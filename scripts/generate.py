import os
import re
import json
import yaml
import glob
import shutil
import random
import textwrap
import requests
from pathlib import Path

# Please dont judge this code. I compensate my lack of jekyll/liquid/yaml experience with python. I need this.

root_dir = Path(__file__).resolve().parent.parent
data_yaml = []
hero_names = []
files = sorted(glob.glob(f"{root_dir}/scripts/bugs/*"), key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
unique_bug_count = len(files)
total_bug_count = 0
print("Connecting to overfast-api...")
response = requests.get("https://overfast-api.tekrop.fr/heroes")
print("Connected.")
download_status = input("Redownload hero portraits? (yes/no) ")

if response.status_code == 200:
    data = response.json()
    hero_count = len(data)
    for hero in data:
        print(f"Gathering data: {hero['name']}")
        data_yaml.append({
            "name": hero['name'],
            "portrait": fr"/assets/images/heroes/{hero['name']}.png",
            "role": hero['role'],
            "bug_count": 0,
        })
        hero_names.append(hero['name'])
        
        if download_status.lower() == "yes":
            url = hero['portrait']
            ext = url[url.rfind("."):] if "." in url else ""
            print(f"Downloading: {hero['name']}.png")
            response = requests.get(url)
            with open(fr"{root_dir}/assets/images/heroes/{hero['name']}{ext}", "wb") as f:
                f.write(response.content)

print(f"Rebuilding hero pages...")

for hero in data_yaml:
    filename = f"{root_dir}/_heroes/{hero['name']}.html"
    
    page = \
f"""---
layout: hero_bugs
title: "FixDoomfist | {hero['name']} bugs"
permalink: "/heroes/{hero['name']}/"
name: "{hero['name']}"
role: "{hero['role']}"
portrait: "{hero['portrait']}"
---""" + """

{% assign bug_count = 0 %}
{% for bug in site.bugs %}
    {% if bug.heroes contains page.name %}
    {% assign bug_count = bug_count | plus: 1 %}
    <div class="separator"><span><b>{{bug_count}}</b></span></div>
        <div class='bug_card'>
            <a href="{{bug.permalink}}"><h2>{{bug.short_name}}</h2></a>
            <p>{{bug.content | markdownify}}</p>
        </div>
    {% endif %}
{% endfor %}"""

    for file in files:
        bug = open(file, "r").read()
        if bug.startswith('---'):
            rest = bug.split('---')
            yaml_data = yaml.safe_load(rest[1])
            if hero['name'] in yaml_data['heroes']:
                data_yaml[hero_names.index(hero['name'])]['bug_count'] += yaml_data['heroes'].count(hero['name'])
                total_bug_count += yaml_data['heroes'].count(hero['name'])
            if type(yaml_data['heroes']) == str:
                if yaml_data['heroes'] not in hero_names and yaml_data['heroes'] != "All heroes":
                    print("ALERM: ", yaml_data['heroes'])
            else:
                for current_hero in yaml_data['heroes']:
                    if current_hero not in hero_names:
                        print("ALERM: ", current_hero)
    with open(filename, 'w+') as f:
        f.write(page)

print("Writing hero bug data...")

with open(f'{root_dir}/_data/heroes.yml', 'w') as f:
    yaml.dump(data_yaml, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Deleting old bug pages...")

bugs = glob.glob(fr"{root_dir}/_bugs/**/*.md")
for bug in bugs:
    os.remove(bug)

print("Rebuilding bug pages...")

count_dict = {
    "total": 0,
    "block": 0,
    "punch": 0,
    "slam": 0,
    "ult": 0,
    "intended": 0,
    "unsolved": 0,
}
for file in files:
    bug = open(file, "r").read()
    if bug.startswith('---'):
        rest = bug.split('---')
        yaml_data = yaml.safe_load(rest[1])
        text = rest[2]
        file_split = file.split('/')
        file_name = file_split[-1]
        file_tags = file_name.split('_')
        file_id = file_tags[0]
        bugged_ability = file_tags[1]
        count_dict[bugged_ability] += 1
        permalink_path_md = '-'.join(file_tags[2:])
        permalink_final = permalink_path_md.split(".")[0]
        if bugged_ability not in ['intended', 'unsolved']:
            count_dict['total'] += 1
            yaml_data['permalink'] = fr"/bugs/{bugged_ability}/{permalink_final}/"
            yaml_data['id'] = file_id
            yaml_data['layout'] = "bug_wiki"
            yaml_data['total_rank'] = count_dict['total']
            yaml_data['ability_rank'] = count_dict[bugged_ability]
            final_yaml = yaml.dump(yaml_data, allow_unicode=True, default_flow_style=False)
            output = f"---\n{final_yaml}---{text}"
        else:
            yaml_data['permalink'] = fr"/bugs/{bugged_ability}/{permalink_final}/"
            yaml_data['id'] = file_id
            yaml_data['layout'] = "bug_wiki"
            yaml_data['ability_rank'] = count_dict[bugged_ability]
            final_yaml = yaml.dump(yaml_data, allow_unicode=True, default_flow_style=False)
            output = f"---\n{final_yaml}---{text}"
        if os.path.isdir(fr'{root_dir}/_bugs/{bugged_ability}'):
            with open(fr'{root_dir}/_bugs/{bugged_ability}/{file_name}', 'w+') as f:
                f.write(output)
        else:
            print(file, fr'{root_dir}/_bugs/{bugged_ability}/{file_name}')
            raise "Dumbass path does not exist"

print("Calculating absurd bug counts...")

jump_in_stun_count = hero_count - 1  # jetpack cat cannot jump
melee_stagger_count = hero_count - 3  # brig and rein dont have melee, and zen melee doesn't reproduce the bug
stair_spot_count = 62 * hero_count  # if i counted correctly, there are 62 known stair spots. every hero (afaik) can connect with them. so.... yea a lot of bugs
absurd_bug_count = unique_bug_count + jump_in_stun_count + melee_stagger_count
ridiculous_bug_count = absurd_bug_count + stair_spot_count

print("Writing bug data...")

bug_yaml_data = {
    "hero_count": hero_count,
    "bug_count": total_bug_count,
    "jump_in_stun_count": jump_in_stun_count,
    "melee_stagger_count": melee_stagger_count,
    "stair_spot_count": stair_spot_count,
    "unique_bug_count": unique_bug_count,
    "absurd_bug_count": absurd_bug_count,
    "ridiculous_bug_count": ridiculous_bug_count,
}

with open(f'{root_dir}/_data/stats.yml', 'w') as f:
    yaml.dump(bug_yaml_data, f, allow_unicode=True, sort_keys=False)

print("Done!")
