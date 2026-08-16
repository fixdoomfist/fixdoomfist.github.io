---
layout: wiki
title: "Doomfist"
permalink: "/heroes/Doomfist/"
name: "Doomfist"
role: "tank"
portrait: "/assets/images/Doomfist.png"
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
<h2>Punch removes stun</h2>
<p>If Doomfist uses Rocket Punch on a stunned enemy, all stun effects will be removed instantly. This does not involve the rooted status effects like Junkrat trap.

It is worth noting that, despite the fact that this interaction is exclusive to Doomfist and not a single other stun ability (i.e. Sigma Rock, Mauga Overrun) behaves in the same way, I've been told by The Hydra List authors that this mechanic is intended. I completely disagree and will continue to treat it as a game-breaking bug.</p></div>

<div class='bug_card'>
<h2>Punch cancel late stalemate</h2>
<p>Doomfist is able to cancel his punch ability by pressing space while keeping the momentum. This “tech” is one of Doomfist’s most core mechanics, used by players of all skill levels. This allows for better map traversal, getting more distance out of an ability, and much more.

But, for a few frames after the ability has been cancelled, the character is still able to be “knocked down” via abilities like Brig Dash or another Doomfist’s Rocket Punch. This leads to him entering the stunned state while still having the momentum of the punch cancel.</p></div>

<div class='bug_card'>
<h2>Camera lock on landing in ult</h2>
<p>If a Doomfist player lands on an “edge” (i.e., the player will immediately start falling once the landing animation is over), the player will be forced to look forward and the camera will be locked in place. It doesn’t matter where the player looked while the landing animation played; when the ultimate ends, the player will be forced to look forward.

# Update as of 12/07/26

Turns out, when you don’t fix bugs, they spread. I’m going to act surprised here.

The camera issue is now also present on moving targets with complex geometry, such as payloads. For now the issue has only been discovered on the map Rialto, but it may also be present on other maps.</p></div>

<div class='bug_card'>
<h2>Slam overrides punch knockback</h2>
<p>If a target is hit by Rocket Punch it will receive knockback. But, if during the time the target is also hit my Seismic Slam, the enemy will stop dead in their tracks.</p></div>

<div class='bug_card'>
<h2>Slowdown when moving up stairs in ult</h2>
<p>Doomfist is unable to go over some elevated floors, even though they can be walked over without jumping.

Most of these instances can be avoided by going at the obstacle at an odd angle or using top-down view, but there is a particularly difficult doorway in King’s Row, so much so that there is a completely separate entry for it in the buglist.</p></div>

<div class='bug_card'>
<h2>Stuck on slopes in ult</h2>
<p>When Doomfist is in his ultimate and is not using the top-down view, he is drastically slowed down when going up any significantly angled surfaces.</p></div>

<div class='bug_card'>
<h2>Magma skin vfx is too bright</h2>
<p>When blocking, the usual “block flash” for the Doomfist mythic skin is just way too bright. It hurts the eye and could be extremely harmful towards people with light sensitivity.</p></div>

<div class='bug_card'>
<h2>Animation issues</h2>
<p>Full credit to `daavel_` from the GetQuakedOn discord server. I did none of the work, but I am willing to take all the credit.

Since the release of Overwatch 2, Doomfist had a lot of animation issues. They don't affect the gameplay in any meaningful way, but should still be considered a bug and fixed.</p></div>