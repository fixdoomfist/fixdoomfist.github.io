---
youtube_link: https://youtu.be/10n279T6PlM
bug_report: https://us.forums.blizzard.com/en/overwatch/t/doomfists-punch-gets-stuck-on-a-deploying-anchor-drone/1014103
heroes: Sierra
credit: Goose
last_tested: 12/08/26
short_name: "Invulnerable Sierra drone"
on_hydra: false
---

Sombra previously had this exact issue, where a thrown translocator would collide with Rocket Punch and stop it as if it hit a player. Anchor Drone, when deployed, does this exact thing without dealing any damage to the drone. Considering that the drone also cannot be shot during this period, I believe it’s a bug and drone collision with Rocket Punch should only be enabled when it is fully deployed.

<!-- SPLIT -->

1. As Doomfist, start charging Rocket Punch while facing Sierra.
2. As Sierra, right before the Doomfist casts Rocket Punch, start placing Anchor Drone directly in his path.
3. Observe how the drone takes no damage as the Doomfist hits it instead of Sierra.
4. If at the moment of impact the drone was far enough away from Sierra, the drone not will take any damage and Sierra will not receive any impact.
