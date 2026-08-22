---
layout: wiki
title: "Junkrat"
permalink: "/heroes/Junkrat/"
name: "Junkrat"
role: "damage"
portrait: "/assets/images/Junkrat.png"
---

<div class='bug_card'>
<h2>Bounced projecitle damage origin</h2>
<p>When projectiles bounce off a wall and hit a blocking Doomfist, the game seems to run a simple calculation to decide if the damage should be blocked or not. It takes the angle at which the projectile bounced off the wall and looks if that angle lands in the block line-of-sight. If it doesn’t, the game assumes that the projectile hit Doomfist in the back, and the damage is not blocked.

However, this simple calculation does not consider hits directly on the Doomfist’s block at steep angles. This leads to characters with projectile-based weapons being able to completely ignore Power Block and deal full damage head-on.</p>
</div>