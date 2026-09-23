---
youtube_link: https://youtu.be/70vzYny6KNw
bug_report: https://us.forums.blizzard.com/en/overwatch/t/doomfist-rocket-punch-acceleration-gets-staggered-by-melee/1017899
heroes: "All heroes"
credit: Goose
last_tested: 12/08/26
short_name: "Punch momentum staggered by melee"
on_hydra: true
---

I believe the issue is specifically caused by any applied horizontal movement (such as knockback with zero vertical velocity) on a grounded Doomfist who is about to use Rocket Punch. For some reason, if Doomfist gets off the ground, the knockback has no effect on the distance traveled, but if he is grounded, it does.

The melee affects the acceleration of Rocket Punch up to the maximum speed value. When punched right before using Rocket Punch, it is noticeably slower, as demonstrated by the video.

This behavior is also shown when using Rocket Punch immediately after Venture's Drill Dash, which pushes Doomfist into the ground. Again, for some reason, horizontal knockback with no verticality affects the acceleration.
