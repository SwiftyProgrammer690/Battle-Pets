from bcolors import bcolors

detailList = [
  bcolors.DARK + "---" + bcolors.ENDC,
  "⚔️ Scratch (0 MP): Scratches the enemy with a basic attack.",
  bcolors.DARK + "⚔️ Claw (2 MP): A lesser attack, but reduces enemy defence slightly." + bcolors.ENDC,
  bcolors.DARK + "🔮 Snare (3 MP): A basic magic move which also increases attack." + bcolors.ENDC,
  bcolors.CYAN + "🔮 Warm Yogurt Slap (3 MP): Magically summon warm yogurt and slap your enemy! Chance to cause poison." + bcolors.ENDC,
  bcolors.DARK + bcolors.CYAN + "🔮 Mega Yogurt Rain (6 MP): Summon huge yogurt from the sky, dealing massive magic damage! Chance to cause deadly poison!" + bcolors.ENDC,
  bcolors.RED + "🔮 Flame (2 MP): Basic flame deals fire damage to the enemy." + bcolors.ENDC,
  bcolors.DARK + bcolors.RED + "🔮 Flameza (5 MP): Mega flame deal massive fire damage. Chance to reduce defence." + bcolors.ENDC,
  bcolors.BLUE + "🔮 Wave (2 MP): Basic water move deals water damage to the enemy." + bcolors.ENDC,
  bcolors.DARK + bcolors.BLUE + "🔮 Waveza (5 MP): Massive wave deals mega water damage. Chance to reduce attack." + bcolors.ENDC,
  bcolors.YELLOW + "🔮 Shock (3 MP): Basic shock is dealt to the enemy. Can cause flinching." + bcolors.ENDC,
  bcolors.DARK + bcolors.YELLOW + "🔮 Shockeza (7 MP): Giant shock nearly fries the enemy. Causes petrify for 2 turns." + bcolors.ENDC,
  bcolors.BLACK + "⚔️ Bash (1 MP): Slightly stronger attack bashes the enemy." + bcolors.ENDC,
  bcolors.BLACK + "⚔️ Barrage (3 MP): Several weak attacks rapidly hit the enemy." + bcolors.ENDC,
  bcolors.PURPLE + "⚔️ Blink (2 MP): A quick sneak attack that ignores 80% of enemy defence." + bcolors.ENDC,
  bcolors.DARK + bcolors.PURPLE + "⚔️ Blinkeza (6 MP): Rapid sneak attacks that ignores 80% of enemy defence." + bcolors.ENDC,
  bcolors.GREEN + "💫 Heal (3 MP): Take a turn to heal yourself" + bcolors.ENDC,
  bcolors.DARK + bcolors.GREEN + "🔮 Leaf Drain (4 MP): Use magic to deal leaf damage while regaining health." + bcolors.ENDC,
  bcolors.PURPLE + "💫 Imbrewence (3 MP): Boosts magic power." + bcolors.ENDC,
  bcolors.DARK + bcolors.YELLOW + "💫 Harden (3 MP): Take a turn to increase defence." + bcolors.ENDC,
  bcolors.DARK + bcolors.YELLOW + "💫 Hardenza (5 MP): Massively increase your defence capability." + bcolors.ENDC,
  bcolors.DARK + bcolors.YELLOW + "⚔️ Rock Wall (6 MP): Slightly increase defence while slamming physical damage on the enemy." + bcolors.ENDC,
  bcolors.RED + "⚔️ Heated Clap (2 MP): Hit a spicy slap while slightly increasing your attack." + bcolors.ENDC,
  "💫 Sword Dance (3 MP): Slightly increase ATTACK and DEFENCE.",
  bcolors.GREEN + "💫 Illinize (3 MP): Inflicts 6 poison on the enemy." + bcolors.ENDC,
  bcolors.DARK + bcolors.GREEN + "💫 Illinizeza (6 MP): Inflicts 12 poison on the enemy." + bcolors.ENDC,
  bcolors.GREEN + "💫 Herbial Treatment (2 MP): Cures poison and any negative statis effects." + bcolors.ENDC,
  bcolors.BLACK + "⚔️ Fakeout (4 MP): Fake out a punch and stagger the enemy." + bcolors.ENDC,
  "⚔️ Double Kick (2 MP): Quick double attack to harm the enemy.",
  bcolors.BLACK + "⚔️ Sharp Slice (1 MP): Very powerful attack, but causes recoil and lost defence." + bcolors.ENDC,
  bcolors.DARK + bcolors.PURPLE + "💫 Withdraw (3 MP): Nerfs enemy magic power." + bcolors.ENDC,
  bcolors.BLACK + "🔮 Dark Sifin (5 MP): Dark magic slightly increases Magic and slightly decreases enemy magic." + bcolors.ENDC,
  bcolors.BLUE + "💫 Focus Energy (2 MP): If enemy attacks, gain extra MP." + bcolors.ENDC,
]

# ⚔️11 🔮11 💫10
# Move list
# 00 ---
# 01 Scratch
# 02 Claw
# 03 Snare
# 04 Warm Yogurt Slap
# 05 Mega Yogurt Rain
# 06 Flame
# 07 Flameza
# 08 Wave
# 09 Waveza
# 10 Shock
# 11 Shockeza
# 12 Bash
# 13 Barrage
# 14 Blink
# 15 Blinkeza
# 16 Heal
# 17 Leaf Drain
# 18 Imbrewence
# 19 Harden
# 20 Hardenza
# 21 Rock Wall
# 22 Heated Clap
# 23 Sword Dance
# 24 Illinize
# 25 Illinizeza
# 26 Herbial Treatment
# 27 Fakeout
# 28 Double Kick
# 29 Sharp Slice
# 30 Withdraw
# 31 Dark Sifin
# 32 Focus Energy
#
# Upcoming
# ?? Buff Dice
# ?? Debuff Dice
# ?? Channel

def grabDetail(id):
    return (detailList[id])

mpRequired = [
  0,2,3,3,6,
  2,5,2,5,3,
  7,1,3,2,6,
  3,4,3,3,5,
  6,2,3,3,6,
  2,4,2,1,3,
  5,2]
