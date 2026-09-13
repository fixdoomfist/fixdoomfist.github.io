---
layout: faq
title: FixDoomfist | FAQ
permalink: /faq/
---

{% assign stats = site.data.stats %}

# When were the bugs last tested?

67/67/6967

# Why?

I have played Overwatch since it came out back in 2016. Since 2019 Doomfist basically never left my hero pool, I have over 150 hours on the character and am extremely passionate about his design and place in the game. I'm doing whatever I can to spread awareness of his gameplay issues in hopes that they become too hard to ignore.

# What is "The Hydra List"?

The Hydra is an extremely important google doc to the community. Authored by Creme and GetQuakedOn, it serves as the main resource for education on the topic of Doomfist bugs. GetQuakedOn also has direct communication with the developers and is able to share feedback directly, so a bug having a spot there generally means better chances of it getting fixed.

# What does it mean when the bug is labeled "All heroes can apply"?

Usually that means the bug is connected to a core gaming mechanic i.e. melee or jumping. These bugs are global and can be replicated with any hero in the game (with a few exceptions i.e. Brigitte and Reinhardt not having a true melee).

# How do I report bugs?

The "official" method is to go to the blizzard forums and make a bug report in the appropriate section. All of the bugs on this website have written up reports, yet they remain unfixed. I believe this is mandatory, but ultimately unlikely to achieve anything.

I personally recommend that, if you are to come across a bug with Doomfist, you should report it in one of the community servers (GetQuakedOn discord server or Doomfist Mains discord server). Either me or someone else that is associated with bug tracking will look at it. An email and a discord/twitter DM may also work, but the response time may wary.

With the bug itself, it's also highly recommended to send the replay code of the game where the bug occurred and a video of it happening.

# This sucks. What can I do about it?

The best thing you can do is spread awareness. Commenting under the bug report posts also helps, since it puts the bug on the front page of the bug report forum. If you see any Doomfist-related bugs in the wild - please send them.

# How are the bugs ranked?

In this website bugs are ranked by how game-breaking I believe they are. The higher the rank, the more important they are to fix. In the intended category they are ranked by how absurd the fact that they will never be fixed is.

# How are the bugs counted?

I try to group bugs by their similarity, and the "total bugs" counter is how many bug groups there is.

"Bugged interactions" are counted by how many each interactions each bug group has, excluding global issues. For example, 7 different characters can replicate "Inconsistent damage origin" bug group, with one of them (Ana) having two bugged interactions in the same group. This means that this one bug group has 8 bugged interactions, and that gives into the count. Global bugs are not counted towards the bugged interactions counter, otherwise it would become too bloated.

# Just how bloated?

Well...

If we also count all global issues towards the bugged interactions count, which is {{stats.jump_in_stun_count}} for jumping in stun plus {{stats.melee_stagger_count}} for melees staggering punch momentum, we get a grand total of {{stats.absurd_bug_count}} bugs!

But... If we also count each known stair spot as an individual bug for each hero that it theoretically can interact with - which is... well.. every hero in the game - we can technically say that Doomfist has {{stats.ridiculous_bug_count}} bugs. How fun.

# Can I help with the website?

This website is hosted on github, which means that the source code of this website is public: you can find a link to it in the resources. Feel free to look for mistakes, bad grammar and everything else you dislike, change it, and send a PR. You can also DM me on discord if you don't want to deal with github and tell me everything directly.
