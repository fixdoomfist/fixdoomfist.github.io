---
layout: wiki
title: "Wuyang"
permalink: "/heroes/Wuyang/"
name: "Wuyang"
role: "support"
portrait: "https://d15f34w2p8l1cc.cloudfront.net/overwatch/4959500b495b35c0908be2abda56b53f2601b2c5cc39a1cfde8df1bffd38d66d.png"
---



<div class='bug_card'>
<h2>Inconsistent damage origin</h2>
<p>The logic behind the game deciding which damage is blocked by the Doomfist and which is not is extremely inconsistent between specific instances. Some abilities are only blocked when the player is actively looking at the character that casted them, even if the point where the ability landed (later 'the origin point' or 'center') is behind Doomfist.

Ana has two bugged interactions:
1. Primary fire. The damage is only blocked if the Doomfist actively looks at Ana. This includes the damage over time, which means that the player can be shot in the back, then look at Ana while the damage is being done, and block most of it.
2. Biotic Grenade. Doomfist can only block Biotic Grenade damage by looking directly at Ana, instead of looking at the center (or the origin point) of the ability.

Zarya: Doomfist can only block Graviton Surge damage by looking directly at Zarya instead of looking at the center (or the origin point) of the ultimate.

Ramattra: Doomfist can only block Ravenous Vortex damage by looking directly at Ramattra, instead of looking at the center (or the origin point) of the ability.

The abilities below are bugged in the same way, but these instances can only be reproduced by using a Symmetra's teleport after the ability has been casted.

Junker Queen: Jagged Knife damage will not be blocked if the Junker Queen throws her blade towards Doomfist's block and teleports behind him before it lands.

Doomfist: Seismic Slam damage will not be blocked if the Doomfist lands his slam in front of a blocking Doomfist and teleports behind him before the ability hits.

Reinhardt: Earthshatter damage will not be blocked if the Reinhardt lands the ult in front of a blocking Doomfist and teleports behind him before the ability hits.

Wuyang: Guardian Wave damage will not be blocked if the Wuyang lands his ability in front of a blocking Doomfist and teleports behind him before the ability hits.</p></div>

<div class='bug_card'>
<h2>Punch momentum override on stairs</h2>
<p>While some abilities like Brig’s Bash or Vendetta’s Overhead Slash can affect Doomfist’s momentum in almost any circumstance, the effect is quite negligible. But, when Doomfist is using Rocket Punch to go up stairs and slopes, the abilities start to tangibly affect the player’s momentum, to the point that a Brigitte’s Bash can completely override Rocket Punch’s movement long enough to change or hinder its trajectory.

The list:
Anran's Inferno Rush, Ashe's Coach Gun, Bastion's A-36 Tactical Grenade, Brigitte's Whip Shot, Domina's Sonic Repulsors, Hazard's Jagged Wall, Illari's Outburst, Jetpack Cat's Purr, Lúcio's Soundwave, Mauga's Overrun, Orisa's Javelin Spin, Pharah's Concussive Blast, Reinhardt's Shield Slam, Roadhog's ult, Shion's Joyride, Vendetta's Whirlwind Dash, Venture's ult, Venture's melee, Winston's ult, Wuyang's Guardian Wave.</p></div>

<div class='bug_card'>
<h2>Punch removes stun</h2>
<p>If Doomfist uses Rocket Punch on a stunned enemy, all stun effects will be removed instantly. This does not involve the rooted status effects like Junkrat trap.

It is worth noting that, despite the fact that this interaction is exclusive to Doomfist and not a single other stun ability (i.e. Sigma Rock, Mauga Overrun) behaves in the same way, I've been told by The Hydra List authors that this mechanic is intended. I completely disagree and will continue to treat it as a game-breaking bug.</p></div>

<div class='bug_card'>
<h2>Punch cooldown not resetting</h2>
<p>Thanks to `itztonii` for providing a fresh clip with the replay code.

This bug remained a mystery for quite some time, but turns out it’s extremely easy to replicate. When you get empowered punch (i.e. the charge bar overfills on the damage) by an ability that stuns you (i.e. Sigma rock or Orisa javelin) and hold the Rocket Punch button at the same time, Rocket Punch goes on cooldown instead of it being reset.</p></div>