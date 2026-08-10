---
layout: wiki
title: "Sigma"
permalink: "/heroes/Sigma/"
name: "Sigma"
role: "tank"
portrait: "https://d15f34w2p8l1cc.cloudfront.net/overwatch/a4c032fa466c9a6d9c6974747635d7ef910027f91cd58892af0c899db565f92d.png"
---

{{page.title}} {{page.name}}


When projectiles bounce off a wall and hit a blocking Doomfist, the game seems to run a simple calculation to decide if the damage should be blocked or not. It takes the angle at which the projectile bounced off the wall and looks if that angle lands in the block line-of-sight. If it doesn’t, the game assumes that the projectile hit Doomfist in the back, and the damage is not blocked.

However, this simple calculation does not consider hits directly on the Doomfist’s block at steep angles. This leads to characters with projectile-based weapons being able to completely ignore Power Block and deal full damage head-on.


If Doomfist uses Rocket Punch on a stunned enemy, all stun effects will be removed instantly. This does not involve the rooted status effects like Junkrat trap.


Thanks to `itztonii` for providing a fresh clip with the replay code.

This bug remained a mystery for quite some time, but turns out it’s extremely easy to replicate. When you get empowered punch (i.e. the charge bar overfills on the damage) by an ability that stuns you (i.e. Sigma rock or Orisa javelin) and hold the Rocket Punch button at the same time, Rocket Punch goes on cooldown instead of it being reset.
