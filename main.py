from PlayerPet import PlayerPet
from EnemyPet import EnemyPet
from ATK_use import grabAtk
from ATK_detail import grabDetail
from ATK_detail import mpRequired
from inventory import inventory
from bcolors import bcolors
import random
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# Thanks internet scources for "bcolors" and "def cls()" :)

def itemEffect(invent, pet, slot):
  if slot == 1:
    pet.hp += 30
    if pet.hp > pet.maxhp:
      pet.hp = pet.maxhp
    print(bcolors.BOLD + bcolors.GREEN + pet.name + " used a Potion and healed 30 HP!")
  if slot == 2:
    pet.mp += 3
    if pet.mp > pet.maxmp:
      pet.mp = pet.maxmp
    print(bcolors.BOLD + bcolors.BLUE + pet.name + " used an Ether and gained 3 MP!" + bcolors.ENDC)
  if slot == 3:
    pet.buffAtk += (3 + round(pet.atk*0.5))
    print(bcolors.BOLD + bcolors.RED + pet.name + " used a Focus Berry and raised their attack!" + bcolors.ENDC)
  if slot == 4:
    pet.buffDf += (3 + round(pet.df*0.5))
    print(bcolors.BOLD + bcolors.YELLOW + pet.name + " used a Plated Berry and raised their defence!" + bcolors.ENDC)
    

def main():
    versionProtocol = 2

    print(bcolors.PURPLE + "Hello!")
    print("Welcome to Battle Pets!\n")

    # print("In the process of updating the game atm :/ .\n")
    print(bcolors.ENDC + bcolors.BOLD + "Version 0.1.3:\n")
    print("There are currently 32 Moves, 13 enemies, and 3 towns.\n" + bcolors.ENDC)
    print("+ 3 New Moves")
    print("+ 2 New Enemies")
    print("+ Added Items. Very basic for now. Currently obtained at a 15% drop rate from enemies.")
    print("* Changed stat boosts, so that they now curve with your current stats.")
    print("* Fixed critical bugs (Out of range skills/item pickups, Withdraw not working correctly, Focus Energy breaking the game.).")
    print("")

    plyPet = PlayerPet("Pet","Balanced",1,0,4,4,4,30,30,0,3,1,0,0)
    plyInvent = inventory(3)


    returning = "d"
    while not returning == "Y" and not returning == "N" and not returning == "n" and not returning == "y":
      returning = input(bcolors.YELLOW + "Are you a returning player? (Y/N)" + bcolors.ENDC)
    
    if returning == "N" or returning == "n":
      needHelp = input("Do you want to hear the basics? (Y/N)")
      if (needHelp == "Y" or needHelp == "y"):
        print(bcolors.PURPLE + "I see you are new. I'll run you through the basics.\n")
        time.sleep(2)
        print("Most decisions in this game will result from the use of numbers (e.g. 1/2/3/4). In the case you say a number incorrectly, in most circumstances you will still be able to type a corrected answer.\n")
        time.sleep(6)
        print("As long as you don't put a letter or nothing you should be good.\n")
        time.sleep(3)
        print("This is a very basic-styled RPG. Most moves are governed by the use of MP which you will recover in battle overtime. And, of course, you will learn different moves from leveling up.\n")
        time.sleep(8)
        print("Including increases in max HP, max MP, ATK, DEF, and MAG. These stats are what tell how much damage you will do depending on the attack and how much enemy hits you can substane. As of now, you will always go first each turn.\n")
        time.sleep(10)

      print("You now must decide what your pet will be...")
      plyPet.name = input(bcolors.YELLOW + "Now tell me... what is your pet's name? (Type any name.)\n" + bcolors.ENDC)
      type1 = 0
      while not type1 == 1 and not type1 == 2 and not type1 == 3:
          type1 = input(plyPet.name + "..." + bcolors.YELLOW + " what does it desire?\n " + bcolors.GREEN + "1) Life (More HP/DEF)...\n " + bcolors.RED + "2) Wrath (More ATK)...\n " + bcolors.BLUE + "3) Intellect (More MAG/MP)...\n" + bcolors.ENDC)
          if not type1 == "":
              type1 = int(type1)
      type2 = 0
      while not type2 == 1 and not type2 == 2 and not type2 == 3:
          type2 = input(bcolors.YELLOW + "What does it leave behind?\n " + bcolors.GREEN + "1) Life (Less HP/DEF)...\n " + bcolors.RED + "2) Wrath (Less ATK)...\n " + bcolors.BLUE + "3) Intellect (Less MAG/MP)...\n" + bcolors.ENDC)
          if not type2 == "":
              type2 = int(type2)

      if type1 == 1:
          if type2 == 1:
              plyPet.type = "Balanced"
          if type2 == 2:
              plyPet.type = "Defensive"
              plyPet.maxhp += 3
              plyPet.df += 1
              plyPet.atk -= 1
          if type2 == 3:
              plyPet.type = "Survival"
              plyPet.maxhp += 3
              plyPet.df += 1
              plyPet.mag -= 1
              plyPet.maxmp -= 1
      if type1 == 2:
          if type2 == 2:
              plyPet.type = "Balanced"
          if type2 == 1:
              plyPet.type = "Berserk"
              plyPet.maxhp -= 3
              plyPet.df -= 1
              plyPet.atk += 2
          if type2 == 3:
              plyPet.type = "Warrior"
              plyPet.maxmp -= 1
              plyPet.mag -= 1
              plyPet.atk += 2
      if type1 == 3:
          if type2 == 3:
              plyPet.type = "Balanced"
          if type2 == 1:
              plyPet.type = "Elf"
              plyPet.maxhp -= 3
              plyPet.df -= 1
              plyPet.mag += 1
              plyPet.maxmp += 1
          if type2 == 2:
              plyPet.type = "Wizard"
              plyPet.maxmp += 1
              plyPet.mag += 1
              plyPet.atk -= 1

      print(bcolors.PURPLE + "I see... You have chosen the " + bcolors.BOLD + bcolors.RED + plyPet.type + bcolors.ENDC + bcolors.PURPLE + " type for your pet...")
      time.sleep(2)
    if returning == "Y" or returning == "y":
      code = input(bcolors.YELLOW + "Please enter your save code. (You cannot copy and paste ;( ) \n" + bcolors.ENDC)
      loadString = code
      x = loadString.split("#")
      print(x)
      print("Save Version " + x[0])
      if x[0] == "1":
          plyPet.name = x[1]
          plyPet.type = x[2]
          plyPet.level = int(x[3])
          plyPet.exp = int(x[4])
          plyPet.atk = int(x[5])
          plyPet.df = int(x[6])
          plyPet.mag = int(x[7])
          plyPet.maxhp = int(x[8])
          plyPet.maxmp = int(x[9])
          plyPet.sp1 = int(x[10])
          plyPet.sp2 = int(x[11])
          plyPet.sp3 = int(x[12])
      if x[0] == "2":
          plyPet.name = x[1]
          plyPet.type = x[2]
          plyPet.level = int(x[3])
          plyPet.exp = int(x[4])
          plyPet.atk = int(x[5])
          plyPet.df = int(x[6])
          plyPet.mag = int(x[7])
          plyPet.maxhp = int(x[8])
          plyPet.maxmp = int(x[9])
          plyPet.sp1 = int(x[10])
          plyPet.sp2 = int(x[11])
          plyPet.sp3 = int(x[12])
          plyInvent.size = int(x[13])
          plyInvent.items[0] = int(x[14])
          plyInvent.amounts[0] = int(x[15])
          plyInvent.items[1] = int(x[16])
          plyInvent.amounts[1] = int(x[17])
          plyInvent.items[2] = int(x[18])
          plyInvent.amounts[2] = int(x[19])
      else:
          print("Invalid code! Defaulting to normal pet.")
    print("Very well... You may continue...\n")
    time.sleep(2)

    cls()

    quit = 0

    town = 1

    while quit == 0:
        print(bcolors.YELLOW + "What will you like to do?\n" + bcolors.ENDC)
        print("1) Find a battle")
        print("2) Inspect your pet")
        print("3) Travel the world")
        print("4) Items")
        print(bcolors.BLACK + "5) Switch Pet" + bcolors.ENDC)
        print("6) Get Code")
        reply = ""
        while reply == "" or reply == 0:
            reply = input("")
            if reply == "1" or reply == "2" or reply == "3" or reply == "4" or reply == "6":
                reply = int(reply)
            else:
              reply == ""
        if reply == 4:
          cls()
          for x in range(0, plyInvent.size):
            print(plyInvent.displayItem(x))
          print("")
          print("1) Throw away item.")
          print("2) Exit back to menu.\n")

          response = 0

          while response == 0:
            response = input(bcolors.YELLOW + "What would you like to do?\n" + bcolors.ENDC)

            if (response == "1"):
              response = 0
              while response == 0:
                response = input(bcolors.YELLOW + "Which one?\n" + bcolors.ENDC)
                success = False
                for x in range(0,plyInvent.size):
                  if response == str(x+1):
                    plyInvent.items[x] = 0
                    plyInvent.amounts[x] = 0
                    success = True
                if (not success):
                  response = 0
            elif response == "2":
              cls()
            else:
              response = 0
            
        if reply == 6:
          print("")
          print("Here is your save code (You cannot copy and paste ;( ):")
          print(bcolors.PURPLE + str(versionProtocol) + "#" + plyPet.name + "#" + plyPet.type + "#" + str(plyPet.level) + "#" + str(plyPet.exp) + "#" + str(plyPet.atk) + "#" + str(plyPet.df) + "#" + str(plyPet.mag) + "#" + str(plyPet.maxhp) + "#" + str(plyPet.maxmp) + "#" + str(plyPet.sp1) + "#" + str(plyPet.sp2) + "#" + str(plyPet.sp3)+ "#" + str(plyInvent.size) + "#" + str(plyInvent.items[0]) + "#" + str(plyInvent.amounts[0]) + "#" + str(plyInvent.items[1]) + "#" + str(plyInvent.amounts[1]) + "#" + str(plyInvent.items[2]) + "#" + str(plyInvent.amounts[2]) + bcolors.ENDC)
        if reply == 2:
            cls()
            print(bcolors.BOLD + plyPet.name + " the " + plyPet.type + " (Level " + str(plyPet.level) + ", " + str(plyPet.exp) + " EXP)" + bcolors.ENDC)
            print(bcolors.GREEN + "Max HP: " + str(plyPet.maxhp))
            print(bcolors.BLUE + "Max MP: " + str(plyPet.maxmp))
            print(bcolors.RED + "ATK: " + str(plyPet.atk) + bcolors.YELLOW + ", DEF: " + str(plyPet.df) + bcolors.PURPLE + ", MAG: " + str(plyPet.mag) + "\n" + bcolors.ENDC)
            print(bcolors.BOLD + "Moves" + bcolors.ENDC)
            print(grabDetail(plyPet.sp1))
            print(grabDetail(plyPet.sp2))
            print(grabDetail(plyPet.sp3))
            print("")
        if reply == 3:
            cls()
            if town == 1:
                print("You are currently at the Pet Ranch.\n Where do you want to go?\n")
            if town == 2:
                print("You are currently at the Yogurt Arena.\n Where do you want to go?\n")
            if town == 3:
                print("You are currently at the Magic Badlands.\n Where do you want to go?\n")
            print("1) Pet Ranch (Recommended for lower level pets.)")
            print(bcolors.CYAN + "2) Yogurt Arena (Recommended for Level 10+ pets.)" + bcolors.ENDC)
            print(bcolors.PURPLE + "3) Magic Badlands (Recommended for Level 20+ pets)" + bcolors.ENDC)

            town = 0
            while not town == "1" and not town == "2" and not town == "3":
                town = (input("\n"))
            town = int(town)
            
            cls()

        if reply == 1:
            plyPet.hp = plyPet.maxhp
            plyPet.mp = int(round(plyPet.maxmp / 2, 0))

            if town == 1:
                select = random.randint(1, 5)
                enyLV = random.randint(0,plyPet.level-1)
                if select == 1:
                    enemy = EnemyPet("Stray L" + str(enyLV+1), 6+enyLV, 4+enyLV, 2, 25+enyLV, 25+(enyLV), 0, 2, 1, 2)
                if select == 2:
                    enemy = EnemyPet("Pitbull L" + str(enyLV+1), 8+enyLV, 1+enyLV, 4, 22+enyLV, 22+enyLV, 0, 4, 1, 3)
                if select == 3:
                    enemy = EnemyPet("Angered Sprinkler L" + str(enyLV+1), 4+enyLV, 7+enyLV, 1, 30+(enyLV*2), 30+(enyLV*2), 1, 5, 1, 8)
                if select == 4:
                    enemy = EnemyPet("Coolio Skunk L" + str(enyLV+1), 5+enyLV, 5+enyLV, 3, 37+(enyLV*2), 37+(enyLV*2), 2, 7, 24, 22)
                if select == 5:
                    enemy = EnemyPet("Bully Bug L" + str(enyLV+1), 7+enyLV, 4+enyLV, 4, 34+(enyLV*2), 24+(enyLV*2), 3, 6, 30, 2)

            if town == 2:
                select = random.randint(1, 5)
                if (plyPet.level > 9):
                  enyLV = random.randint(0,plyPet.level-10)
                else:
                  enyLV = 0
                if select == 1:
                    enemy = EnemyPet("Yogurt Man L" + str(enyLV+10), 8+enyLV, 13+enyLV, 9, 45+(enyLV*2), 45+(enyLV*2), 2, 6, 1, 4)
                if select == 2:
                    enemy = EnemyPet("Slap Enthusiast L" + str(enyLV + 10), 14+enyLV, 4+enyLV, 7, 52+(enyLV*2), 52+(enyLV*2), 1, 5, 12, 13)
                if select == 3:
                    enemy = EnemyPet("Spicy Boi L" + str(enyLV + 10), 17+enyLV, 14+enyLV, 8, 49+(enyLV*2), 49+(enyLV*2), 1, 6, 22, 4)
                if select == 4:
                    enemy = EnemyPet("Charger L" + str(enyLV + 10), 15+enyLV, 10+enyLV, 5, 50+(enyLV*2),50+(enyLV*2), 7, 20, 23, 1)
                if select == 5:
                    enemy = EnemyPet("Slueth L" + str(enyLV + 10), 8+enyLV, 17+enyLV, 5, 47+(enyLV*2),47+(enyLV*2), 5, 10, 32, 31)
            if town == 3:
                select = random.randint(1,3)
                if (plyPet.level > 19):
                  enyLV = random.randint(0,plyPet.level-20)
                else:
                  enyLV = 0
                if select == 1:
                  enemy = EnemyPet("Rockbreaker L" + str(enyLV+20), 30+enyLV, 17+enyLV, 20, 88+(enyLV*3), 88+(enyLV*3), 7, 10, 21, 19)
                if select == 2:
                  enemy = EnemyPet("Grand Shocker L" + str(enyLV+20), 15+enyLV, 33+enyLV, 15, 82+(enyLV*3), 82+(enyLV*3), 8, 12, 11, 9)
                if select == 3:
                  enemy = EnemyPet("Master Poisoner L" + str(enyLV+20), 0+enyLV, 0+enyLV, 20, 80+(enyLV*3), 80+(enyLV*3), 12, 21, 25, 26)

            cls()

            print("A wild " + bcolors.BOLD + enemy.name + bcolors.ENDC + " appeared!")

            battle = True

            while battle:


                if plyPet.buffPoison > 0:
                    print(plyPet.name + " > " + bcolors.GREEN + "HP: " + str(plyPet.hp) + bcolors.PURPLE + " (POISONED: " + str(plyPet.buffPoison) + ") " + bcolors.ENDC + " / " + bcolors.BLUE + "MP: " + str(plyPet.mp) + bcolors.ENDC)
                else:
                    print(plyPet.name + " > " + bcolors.GREEN + "HP: " + str(plyPet.hp) + bcolors.ENDC + " / " + bcolors.BLUE + "MP: " + str(plyPet.mp) + bcolors.ENDC)
                
                if not plyPet.buffAtk == 0:
                  if plyPet.buffAtk > 0:
                    print(bcolors.RED + "ATK: +" + str(plyPet.buffAtk) + " " + bcolors.ENDC, end = '')
                  else:
                    print(bcolors.RED + "ATK: " + str(plyPet.buffAtk) + " " + bcolors.ENDC, end = '')
                if not plyPet.buffMag == 0:
                  if plyPet.buffMag > 0:
                    print(bcolors.PURPLE + "MAG: +" + str(plyPet.buffMag) + " " + bcolors.ENDC, end = '')
                  else:
                    print(bcolors.PURPLE + "MAG: " + str(plyPet.buffMag) + " " + bcolors.ENDC, end = '')
                if not plyPet.buffDf == 0:
                  if plyPet.buffDf > 0:
                    print(bcolors.YELLOW + "DEF: +" + str(plyPet.buffDf) + " " + bcolors.ENDC, end = '')
                  else:
                    print(bcolors.YELLOW + "DEF: " + str(plyPet.buffDf) + " " + bcolors.ENDC, end = '')
                if not plyPet.buffMPRage == 0:
                    print(bcolors.BLUE + "FOCUS: " + str(plyPet.buffMPRage) + " " + bcolors.ENDC, end = '')
                
                print("\n")

                if enemy.buffPoison > 0:
                    print(enemy.name + " > " + bcolors.GREEN + "HP: " + str(enemy.hp) + bcolors.PURPLE + " (POISONED: " + str(enemy.buffPoison) + ") " + bcolors.ENDC + " / " + bcolors.BLUE + "MP: " + str(enemy.mp) + bcolors.ENDC)
                else:
                    print(bcolors.RED + enemy.name + " > " + bcolors.GREEN + "HP: " + str(enemy.hp) + bcolors.ENDC + " / " + bcolors.BLUE + "MP: " + str(enemy.mp) + bcolors.ENDC)
                
                if not enemy.buffAtk == 0:
                  if enemy.buffAtk > 0:
                    print(bcolors.RED + "ATK: +" + str(enemy.buffAtk) + " " + bcolors.ENDC, end = '')
                  else:
                    print(bcolors.RED + "ATK: " + str(enemy.buffAtk) + " " + bcolors.ENDC, end = '')
                if not enemy.buffMag == 0:
                  if enemy.buffMag > 0:
                    print(bcolors.PURPLE + "MAG: +" + str(enemy.buffMag) + " " + bcolors.ENDC, end = '')
                  else:
                    print(bcolors.PURPLE + "MAG: " + str(enemy.buffMag) + " " + bcolors.ENDC, end = '')
                if not enemy.buffDf == 0:
                  if enemy.buffDf > 0:
                    print(bcolors.YELLOW + "DEF: +" + str(enemy.buffDf) + " " + bcolors.ENDC, end = '')
                  else:
                    print(bcolors.YELLOW + "DEF: " + str(enemy.buffDf) + " " + bcolors.ENDC, end = '')
                if not enemy.buffMPRage == 0:
                    print(bcolors.BLUE + "FOCUS: " + str(enemy.buffMPRage) + " " + bcolors.ENDC, end = '')
                
                print("\n")

                print(grabDetail(plyPet.sp1))
                print(grabDetail(plyPet.sp2))
                print(grabDetail(plyPet.sp3))
                print("Pass: Pass this turn, gain extra MP.")
                print("Item: Use an item.")
                plyInput = 0
                mpPassed = False
                if plyPet.buffPetrify == 0:
                    while plyInput == 0 and not mpPassed == True:
                        plyInput = (input("Choose an option (1/2/3/4/5)\n"))
                        if  plyInput == "1" or plyInput == "2" or plyInput == "3" or plyInput == "4"or plyInput == "5":
                            plyInput = int(plyInput)
                        else:
                          plyInput == 0
                        if (plyInput == 1):
                            if (plyPet.mp < mpRequired[plyPet.sp1 - 1]):
                                print(bcolors.RED + "You do not have enough MP to use this move!" +  bcolors.ENDC)
                                mpPassed = False
                                plyInput = 0
                            else:
                                mpPassed = True
                        if (plyInput == 2):
                            if (plyPet.mp < mpRequired[plyPet.sp2 - 1]):
                                print(bcolors.RED + "You do not have enough MP to use this move!" +  bcolors.ENDC)
                                mpPassed = False
                                plyInput = 0
                            else:
                                mpPassed = True
                        if (plyInput == 3):
                            if (plyPet.mp < mpRequired[plyPet.sp3 - 1]):
                                print(bcolors.RED + "You do not have enough MP to use this move!" +  bcolors.ENDC)
                                mpPassed = False
                                plyInput = 0
                            else:
                                mpPassed = True
                        if (plyInput == 4):
                            plyPet.mp += 1
                            mpPassed = True
                            print(plyPet.name + " passes!")
                        if (plyInput == 5):
                          print("")
                          for x in range(0, plyInvent.size):
                            print(plyInvent.displayItem(x))
                          print("")
                          usedSlot = input(bcolors.YELLOW + "Which item do you want to use?\n" + bcolors.ENDC)
                          usedSlotSuccess = -1
                          usedSlot = int(usedSlot)-1
                          if not plyInvent.amounts[usedSlot] == 0:
                            usedSlotSuccess = plyInvent.items[usedSlot]
                            plyInvent.subtractItem(usedSlot,1)
                          if (usedSlotSuccess == -1):
                            plyInput = 0


                    cls()

                    if (plyInput == 1):
                        enemy.hp -= (grabAtk(plyPet.sp1, plyPet.name, (plyPet.atk+plyPet.buffAtk), (plyPet.mag+plyPet.buffMag), plyPet.mp, (enemy.df+enemy.buffDf)))
                        plyPet.mp -= mpRequired[plyPet.sp1 - 1]
                        enemy.Debuff(plyPet.sp1)
                        plyPet.Buff(plyPet.sp1)
                    if (plyInput == 2):
                        enemy.hp -= (grabAtk(plyPet.sp2, plyPet.name, (plyPet.atk+plyPet.buffAtk), (plyPet.mag+plyPet.buffMag), plyPet.mp, (enemy.df+enemy.buffDf)))
                        plyPet.mp -= mpRequired[plyPet.sp2 - 1]
                        enemy.Debuff(plyPet.sp2)
                        plyPet.Buff(plyPet.sp2)
                    if (plyInput == 3):
                        enemy.hp -= (grabAtk(plyPet.sp3, plyPet.name, (plyPet.atk+plyPet.buffAtk), (plyPet.mag+plyPet.buffMag), plyPet.mp, (enemy.df+enemy.buffDf)))
                        plyPet.mp -= mpRequired[plyPet.sp3 - 1]
                        enemy.Debuff(plyPet.sp3)
                        plyPet.Buff(plyPet.sp3)
                    if (plyInput == 4):
                            print(plyPet.name + " passes!")
                    if (plyInput == 5):
                      itemEffect(plyInvent, plyPet, usedSlotSuccess)

                else:
                    print(plyPet.name + bcolors.RED + " is unable to attack!" + bcolors.ENDC)
                    plyPet.buffPetrify -= 1

                enemy.statusEffects()

                print("")

                plyPet.mp += 1

                time.sleep(2)

                if plyPet.mp > plyPet.maxmp:
                    plyPet.mp = plyPet.maxmp


                if enemy.hp < 1:
                    battle = False
                if battle == True:
                    if enemy.buffPetrify == 0:
                        enemyChoice = random.randint(1, 2)
                        if enemyChoice == 1:
                            if (enemy.mp < mpRequired[enemy.atk1 - 1]):
                                print("Enemy passes!")
                                enemy.mp += 1
                            else:
                                plyPet.hp -= (grabAtk(enemy.atk1, enemy.name, (enemy.atk+enemy.buffAtk), (enemy.mag+enemy.buffMag), enemy.mp, (plyPet.df+plyPet.buffDf)))
                                enemy.mp -= mpRequired[enemy.atk1 - 1]
                                plyPet.Debuff(enemy.atk1)
                                enemy.Buff(enemy.atk1)
                        if enemyChoice == 2:
                            if (enemy.mp < mpRequired[enemy.atk2 - 1]):
                                print("Enemy passes!")
                                enemy.mp += 1
                            else:
                                plyPet.hp -= (grabAtk(enemy.atk2, enemy.name, (enemy.atk+enemy.buffAtk), (enemy.mag+enemy.buffMag), enemy.mp, (plyPet.df+plyPet.buffDf)))
                                enemy.mp -= mpRequired[enemy.atk2 - 1]
                                plyPet.Debuff(enemy.atk2)
                                enemy.Buff(enemy.atk2)
                    else:
                        print(enemy.name + bcolors.RED + " is unable to attack!" + bcolors.ENDC)
                        enemy.buffPetrify -= 1

                    plyPet.statusEffects()
                    time.sleep(2)

                    print("")

                    enemy.mp += 1

                if plyPet.hp < 1:
                    battle = False

            if (enemy.hp) < 1:

                cls()

                print(plyPet.name + " wins!\n")

                townindex = [1,10,20]
                plyPet.exp += enyLV+townindex[town-1]

                if random.randint(0,100) > 84:
                  item = random.randint(1,4)
                  if plyInvent.addItem(item, 1):
                    print(plyPet.name + " has found a " + plyInvent.descriptions[item])
                    time.sleep(2)


                if plyPet.exp > (plyPet.level-1):
                    plyPet.level += 1
                    print(bcolors.BOLD + plyPet.name + " has leveled up!\n" + bcolors.ENDC)
                    plyPet.lvlup()

                    time.sleep(1)

                    if plyPet.level % 2 == 0:
                        if town == 1:
                          availableskills = [1,2,3,6,8,10,18,19,23,28]
                          newskill = availableskills[random.randint(0, 9)]
                        if town == 2:
                          availableskills = [6,8,10,14,12,4,16,22,23,24,26,27,29,30,31,32]
                          newskill = availableskills[random.randint(0, 15)]
                        if town == 3:
                          availableskills = [7,9,11,20,21,17,16,15,24,29,25,26,31,32]
                          newskill = availableskills[random.randint(0, 13)]
                        
                        print("You can learn a new skill. Which do you want to replace? (1/2/3, 4 for disregard)")
                        print(grabDetail(newskill))
                        print("")
                        print(grabDetail(plyPet.sp1))
                        print(grabDetail(plyPet.sp2))
                        print(grabDetail(plyPet.sp3) + "\n")
                        chosen = 0
                        while chosen == 0:
                            chosen = int(input(""))
                            if chosen == 1:
                                plyPet.sp1 = newskill
                            elif chosen == 2:
                                plyPet.sp2 = newskill
                            elif chosen == 3:
                                plyPet.sp3 = newskill
                            elif chosen == 4:
                                print("You disregard the new skill.")
                            else:
                                chosen = 0
                        cls()


            if (plyPet.hp) < 1:
                print(bcolors.BOLD + bcolors.RED + plyPet.name + " loses! Maybe try training more?" + bcolors.ENDC)

            plyPet.reset()
            enemy.reset()








if __name__ == "__main__":
    main()
