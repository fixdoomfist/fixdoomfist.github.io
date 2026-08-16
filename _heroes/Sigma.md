---
layout: wiki
title: "Sigma"
permalink: "/heroes/Sigma/"
name: "Sigma"
role: "tank"
portrait: "/assets/images/Sigma.png"
---



<div class='bug_card'>
<h2>Bounced projecitle damage origin</h2>
<p>When projectiles bounce off a wall and hit a blocking Doomfist, the game seems to run a simple calculation to decide if the damage should be blocked or not. It takes the angle at which the projectile bounced off the wall and looks if that angle lands in the block line-of-sight. If it doesn’t, the game assumes that the projectile hit Doomfist in the back, and the damage is not blocked.

However, this simple calculation does not consider hits directly on the Doomfist’s block at steep angles. This leads to characters with projectile-based weapons being able to completely ignore Power Block and deal full damage head-on.</p></div>

<div class='bug_card'>
<h2>Punch removes stun</h2>
<p>If Doomfist uses Rocket Punch on a stunned enemy, all stun effects will be removed instantly. This does not involve the rooted status effects like Junkrat trap.

It is worth noting that, despite the fact that this interaction is exclusive to Doomfist and not a single other stun ability (i.e. Sigma Rock, Mauga Overrun) behaves in the same way, I've been told by The Hydra List authors that this mechanic is intended. I completely disagree and will continue to treat it as a game-breaking bug.</p></div>

<div class='bug_card'>
<h2>Punch cooldown not resetting</h2>
<p>Thanks to `itztonii` for providing a fresh clip with the replay code.

This bug remained a mystery for quite some time, but turns out it’s extremely easy to replicate. When you get empowered punch (i.e. the charge bar overfills on the damage) by an ability that stuns you (i.e. Sigma rock or Orisa javelin) and hold the Rocket Punch button at the same time, Rocket Punch goes on cooldown instead of it being reset.</p></div>