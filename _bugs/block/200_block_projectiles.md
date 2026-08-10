---
youtube_link: https://youtu.be/Cbi0p02BoMU
bug_report: https://us.forums.blizzard.com/en/overwatch/t/doomfist-does-not-block-bounced-projectiles-properly/1029577
heroes:
    - Sigma
    - Junkrat
    - Hanzo
    - Mizuki
credit: Goose
---

When projectiles bounce off a wall and hit a blocking Doomfist, the game seems to run a simple calculation to decide if the damage should be blocked or not. It takes the angle at which the projectile bounced off the wall and looks if that angle lands in the block line-of-sight. If it doesn’t, the game assumes that the projectile hit Doomfist in the back, and the damage is not blocked.

However, this simple calculation does not consider hits directly on the Doomfist’s block at steep angles. This leads to characters with projectile-based weapons being able to completely ignore Power Block and deal full damage head-on.
