---
ability_rank: 1
bug_report:
- https://us.forums.blizzard.com/en/overwatch/t/doomfist-block-logic-is-extremely-inconsisntent/985284
- https://us.forums.blizzard.com/en/overwatch/t/doomfist-block-logic-is-extremely-inconsisntent-cont/997116
credit: The Hydra List
heroes:
- Ana
- Ana
- Zarya
- Ramattra
- Junker Queen
- Doomfist
- Reinhardt
- Wuyang
heroes_affected: 7
id: '0100'
last_tested: 12/08/26
layout: bug_wiki
on_hydra: true
permalink: /bugs/block/logic/
short_name: Inconsistent damage origin
total_rank: 1
youtube_link:
- https://youtu.be/XyuGykiCtVA
- https://youtu.be/nHlEHwvVaUk
---

The logic of the game determining which damage is blocked by Doomfist and which is not is extremely inconsistent in certain instances. In some cases, abilities are only blocked when the player is facing the character that cast them, even if the point where the ability landed (later referred to as 'the origin point' or 'center') is behind Doomfist.

Ana has two bugged interactions:
1. Primary fire: The damage is only blocked if the Doomfist actively looks at Ana. This includes the damage over time, which means that the player can be shot in the back, then look at Ana while the damage is being done, and block most of it.
2. Biotic Grenade: Doomfist can only block Biotic Grenade damage by looking directly at Ana, instead of looking at the center (or the origin point) of the ability.

Zarya: Doomfist can only block Graviton Surge damage by looking directly at Zarya instead of looking at the center (or the origin point) of the ultimate.

Ramattra: Doomfist can only block Ravenous Vortex damage by looking directly at Ramattra, instead of looking at the center (or the origin point) of the ability.

The abilities below are bugged in the same way, but these instances can only be reproduced by using a Symmetra's teleport after the ability has been casted.

Junker Queen: Jagged Knife damage will not be blocked if the Junker Queen throws her blade towards Doomfist's block and teleports behind him before it lands.

Doomfist: Seismic Slam damage will not be blocked if the Doomfist lands his slam in front of a blocking Doomfist and teleports behind him before the ability hits.

Reinhardt: Earthshatter damage will not be blocked if the Reinhardt lands the ult in front of a blocking Doomfist and teleports behind him before the ability hits.

Wuyang: Guardian Wave damage will not be blocked if the Wuyang lands his ability in front of a blocking Doomfist and teleports behind him before the ability hits.

<!-- SPLIT -->

Ana Biotic Grenade example:

1. As Doomfist, start blocking while facing directly towards Ana.
2. As Ana, throw the Biotic Grenade behind the blocking Doomfist, ensuring it still hits him.
3. Observe as the damage from the ability is blocked.
4. Repeat the steps but, instead of looking towards Ana, look at the spot where the ability is going to land instead.
5. Observe the damage not being blocked if the Doomfist is not facing the Ana.
