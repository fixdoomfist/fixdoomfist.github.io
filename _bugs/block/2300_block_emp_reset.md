---
ability_rank: 6
bug_report: https://us.forums.blizzard.com/en/overwatch/t/doomfists-punch-cooldown-does-not-reset-on-being-empowered/1014811
credit: Goose
heroes:
- Ana
- Orisa
- Reinhardt
- Sigma
heroes_affected: 4
id: '2300'
last_tested: 12/08/26
layout: bug_wiki
on_hydra: true
permalink: /bugs/block/emp-reset/
short_name: Punch cooldown not resetting
total_rank: 25
youtube_link: https://youtu.be/cLZVs5a_h7I
---

Thanks to `itztonii` for providing a fresh clip with the replay code.

This bug has been a mystery for some time, but it turns out that it can be easily replicated. When you receive empowered punch (i.e., the charge bar overfills due to damage) from an ability that stuns you (i.e., Sigma's rock or Orisa's javelin), and hold down the Rocket Punch button simultaneously, once you get stunned, Rocket Punch goes on cooldown instead of being reset.

Confirmed stun abilities list: Ana's Sleep Dart, Orisa's Energy Javelin, Reinhardt's Earthshatter, Sigma's Accretion.

<!-- SPLIT -->

1. As Doomfist, start blocking and have the "block meter" be almost filled.
2. Start holding the Rocket Punch button (default: RMB).
3. Get hit with Sigma's Accretion while still blocking and holding the button.
4. Observe how Doomfist's Rocket Punch is on full cooldown rather than being reset.
