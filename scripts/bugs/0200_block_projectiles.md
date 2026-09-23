---
youtube_link: https://youtu.be/Cbi0p02BoMU
bug_report: https://us.forums.blizzard.com/en/overwatch/t/doomfist-does-not-block-bounced-projectiles-properly/1029577
heroes:
    - Sigma
    - Junkrat
    - Hanzo
    - Mizuki
credit: Goose
last_tested: 12/08/26
short_name: "Bounced projecitle damage origin"
on_hydra: true
---

When projectiles bounce off a wall and hit a blocking Doomfist, the game appears to use a simple calculation to determine if the damage should be blocked or not. It checks the angle at which the projectile bounced off the wall and looks to see if that angle falls within the block line-of-sight. If it does not, the game assumes that the projectile hit Doomfist from behind, and the damage is not blocked.

However, this simple calculation does not account for hits directly on Doomfist's block at steep angles. This allows characters with projectile-based weapons to bypass Power Block and deal full damage head-on.
