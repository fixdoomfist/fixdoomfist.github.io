---
layout: wiki
title: "Mizuki"
permalink: "/heroes/Mizuki/"
name: "Mizuki"
role: "support"
portrait: "https://d15f34w2p8l1cc.cloudfront.net/overwatch/a9733c2367e0cbd70b9316fd2e1e17028653ec56d0051ea6ff098531dc4f99fc.png"
---



<div class='bug_card'>
<h2>Bounced projecitle damage origin</h2>
<p>When projectiles bounce off a wall and hit a blocking Doomfist, the game seems to run a simple calculation to decide if the damage should be blocked or not. It takes the angle at which the projectile bounced off the wall and looks if that angle lands in the block line-of-sight. If it doesn’t, the game assumes that the projectile hit Doomfist in the back, and the damage is not blocked.

However, this simple calculation does not consider hits directly on the Doomfist’s block at steep angles. This leads to characters with projectile-based weapons being able to completely ignore Power Block and deal full damage head-on.</p></div>

<div class='bug_card'>
<h2>Casting abilities while stunned by punch</h2>
<p>Credit for most of the interaction is with The Hydra List.

When Doomfist hits anyone with his Rocket Punch, all abilities that the hit character was casting are instantly canceled. This is intuitive. If you hit a Mercy that is trying to resurrect someone - the resurrect is canceled. Simple as. But some abilities are unable to be canceled, even though they should be.

The list includes:
Winston (Melee in Primal), Echo (Cancel Flight), Hanzo (Cancel Storm Arrows), Hazard (Cancel Jagged Wall), Soldier: 76 (Biotic Field), Baptiste (Regenerative Burst & Exo Boots), Lifeweaver (Cancel Tree), Zenyatta (Orb of Destruction Alt Fire), Illari (Cancel Pylon), Emre (Cancel Siphon Blaster), Mizuki (Ultimate), D.Mon (Cancel Fusion Repeater).</p></div>