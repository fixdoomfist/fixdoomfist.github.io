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
files = sorted(glob.glob(f"{root_dir}/scripts/bugs/*"), key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))  # im so fr idk what this does and i dont remember writing this. if it works it works ig
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
    
    # messy? yes. works? without a hitch
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
            {% if bug.path contains '_bugs/intended/' %}
                <a href="{{bug.permalink}}"><h2>[INTENDED] {{bug.short_name}}</h2></a>
            {% elsif bug.path contains '_bugs/unsolved' %}
                <a href="{{bug.permalink}}"><h2>[UNSOLVED] {{bug.short_name}}</h2></a>
            {% else %}
                <a href="{{bug.permalink}}"><h2>{{bug.short_name}}</h2></a>
            {% endif %}
            <p>{{bug.content | markdownify}}</p>
        </div>
    {% endif %}
{% endfor %}"""

    for file in files:
        bug = open(file, "r").read()
        if bug.startswith('---'):
            # splitting front matter and processing it as yaml
            bug_text = bug.split('---')
            yaml_data = yaml.safe_load(bug_text[1])
            file_split = file.split('/')
            file_name = file_split[-1]
            file_tags = file_name.split('_')
            bugged_ability = file_tags[1]
            
            # yes its messy. but it works so i dont careee i love it
            if hero['name'] in yaml_data['heroes'] and bugged_ability not in ['intended', 'unsolved']:
                data_yaml[hero_names.index(hero['name'])]['bug_count'] += yaml_data['heroes'].count(hero['name'])
                total_bug_count += yaml_data['heroes'].count(hero['name'])

            # simple check for wrong hero names. this is how i found out that the wold "Soldier" is typed like that and not "Solider". Wrote it like "Solider" for my whole 18 years btw
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

# used for ranking
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
        # splitting front matter and processing it as yaml
        bug_text = bug.split('---')
        yaml_data = yaml.safe_load(bug_text[1])
        text = bug_text[2]

        # splitting file name to get category and id
        file_split = file.split('/')
        file_name = file_split[-1]
        file_tags = file_name.split('_')
        file_id = file_tags[0]
        bugged_ability = file_tags[1]
        count_dict[bugged_ability] += 1

        # permalink from category
        permalink_path_md = '-'.join(file_tags[2:])
        permalink_final = permalink_path_md.split(".")[0]

        # adding yaml data that i cant be arsed to make in liquid (whole reason this script exists)
        yaml_data['permalink'] = fr"/bugs/{bugged_ability}/{permalink_final}/"
        yaml_data['id'] = file_id
        yaml_data['layout'] = "bug_wiki"
        yaml_data['ability_rank'] = count_dict[bugged_ability]
        if type(yaml_data['heroes']) == str:
            if yaml_data['heroes'] == "All heroes":
                yaml_data['heroes_affected'] = hero_count
            else:
                yaml_data['heroes_affected'] = 1
        else:
            yaml_data['heroes_affected'] = len(set(yaml_data['heroes']))

        # dont count bugs in these categories to the total count
        if bugged_ability not in ['intended', 'unsolved']:
            count_dict['total'] += 1
            yaml_data['total_rank'] = count_dict['total']

        final_yaml = yaml.dump(yaml_data, allow_unicode=True, default_flow_style=False)
        output = f"---\n{final_yaml}---{text}"

        # writing
        if os.path.isdir(fr'{root_dir}/_bugs/{bugged_ability}'):
            with open(fr'{root_dir}/_bugs/{bugged_ability}/{file_name}', 'w+') as f:
                f.write(output)
        else:
            print(file, fr'{root_dir}/_bugs/{bugged_ability}/{file_name}')
            raise "Category does not have a dir in _bugs"

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

# making sass-available data
bug_sass_data = \
f"""$bug-count: (
    punch: {count_dict['punch']},
    block: {count_dict['block']},
    slam: {count_dict['slam']},
    ult: {count_dict['ult']},
);

$abilities: punch, block, slam, ult;"""

with open(fr'{root_dir}/_sass/stats.sass', 'w+') as f:
    f.write(bug_sass_data)

print("Done!")
