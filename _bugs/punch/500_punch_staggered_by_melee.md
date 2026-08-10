---
youtube_link: https://youtu.be/70vzYny6KNw
bug_report: https://us.forums.blizzard.com/en/overwatch/t/doomfist-rocket-punch-acceleration-gets-staggered-by-melee/1017899
heroes: "All heroes"
credit: Goose
---

I believe the issue is specifically caused by any applied horizontal movement, that does not make Doomfist get off the ground (i.e. knockback has zero vertical velocity. Melee is, basically, the only example of that in the game), on a grounded Doomfist that is about to use Rocket Punch. For some reason, if Doomfist gets off the ground, the knockback has no effect on the distance traveled, but if he is grounded, it does.

The melee affects the acceleration of Rocket Punch up to the maximum speed value. When punched right before, it is noticeably slower, demonstrated by the video.

This behavior is also shown when using Rocket Punch right after Venture’s Drill Dash that pushes Doomfist into the ground. Again, for some reason, horizontal knockback with no verticality affects the acceleration.
