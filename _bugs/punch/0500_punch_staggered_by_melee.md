---
ability_rank: 2
bug_report: https://us.forums.blizzard.com/en/overwatch/t/doomfist-rocket-punch-acceleration-gets-staggered-by-melee/1017899
credit: Goose
heroes: All heroes
heroes_affected: 53
id: '0500'
last_tested: 12/08/26
layout: bug_wiki
on_hydra: true
permalink: /bugs/punch/staggered-by-melee/
short_name: Punch momentum staggered by melee
total_rank: 4
youtube_link: https://youtu.be/70vzYny6KNw
---

I believe the issue is specifically caused by any applied horizontal movement (such as knockback with zero vertical velocity) on a grounded Doomfist who is about to use Rocket Punch. For some reason, if Doomfist gets off the ground, the knockback has no effect on the distance traveled, but if he is grounded, it does.

The melee affects the acceleration of Rocket Punch up to the maximum speed value. When punched right before using Rocket Punch, it is noticeably slower, as demonstrated by the video.

This behavior is also shown when using Rocket Punch immediately after Venture's Drill Dash, which pushes Doomfist into the ground. Again, for some reason, horizontal knockback with no verticality affects the acceleration.

<!-- SPLIT -->

1. As Doomfist, start charging Rocket Punch in any direction.
2. Cast the ability and mark the spot where the Doomfist has reached.
3. Now start charging Rocket Punch from the same exact spot in the same direction.
4. As an enemy, stand next to the Doomfist and hit him with a melee right as he starts to cast his ability.
5. Observe how the Doomfist has covered less distance compared to the first cast.
