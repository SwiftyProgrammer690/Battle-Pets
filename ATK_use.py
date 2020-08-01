import time
import random
from bcolors import bcolors

moveBASE = [3,0]
moveATK = [1,1]
moveMAG = [0,0]
moveMPMULTI = [1,1]
moveOPPODEFMULTI = [1,1]
moveREPEATS = [0,0]

moveCOLORS = [
  bcolors.BOLD,
  bcolors.BOLD + bcolors.DARK]
moveDISPLAY = [
  " uses Scratch!",
  " uses Claw!"]


def grabAtk(id, name, atk, mag, mp, oppo_def):
    varience = random.randint(0, 5) - 3
    if id == 1:
        print(moveCOLORS[id-1] + name + moveDISPLAY[id-1] + bcolors.ENDC)

        if (atk*moveATK[id-1] + mp*moveMPMULTI[id-1] + moveBASE[id-1] - oppo_def*moveOPPODEFMULTI[id-1] + varience > 0):
            print("It deals " + str(atk*moveATK[id-1] + mp*moveMPMULTI[id-1] + moveBASE[id-1] - oppo_def*moveOPPODEFMULTI[id-1] + varience))
            return (atk*moveATK[id-1] + mp*moveMPMULTI[id-1] + moveBASE[id-1] - oppo_def*moveOPPODEFMULTI[id-1] + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 2:
        print(bcolors.BOLD + bcolors.DARK + name + " uses Claw!" + bcolors.ENDC)
        if (atk + mp - oppo_def + varience > 0):
            print("It deals " + str(atk + mp - oppo_def + varience))
            return (atk + mp - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 3:
        print(bcolors.BOLD + bcolors.DARK + name + " uses Snare!" + bcolors.ENDC)
        if (mag + 2 + mp - oppo_def + varience > 0):
            print("It deals " + str(mag + 2 + mp - oppo_def + varience))
            return (mag + 2 + mp - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 4:
        print(bcolors.BOLD + bcolors.CYAN + name + " uses Warm Yogurt Slap!" + bcolors.ENDC)
        if (mag + 6 + mp - oppo_def + varience > 0):
            print("It deals " + str(mag + 6 + mp - oppo_def + varience))
            return (mag + 6 + mp - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 5:
        print(bcolors.BOLD + bcolors.CYAN + name + " uses Mega Yogurt Rain!" + bcolors.ENDC)
        if (mag + 22 + mp*2 - oppo_def + varience > 0):
            print("It deals " + str(mag*2 + 22 + mp*2 - oppo_def + varience))
            return (mag + 22 + mp*2 - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 6:
        print(bcolors.BOLD + bcolors.RED + name + " uses Flame!" + bcolors.ENDC)
        if (mag + mp - oppo_def + varience > 0):
            print("It deals " + str(mag + mp - oppo_def + varience))
            return (mag + mp - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 7:
        print(bcolors.BOLD + bcolors.RED + name + " uses Flameza!" + bcolors.ENDC)
        if (10 + mag + mp*2 - oppo_def + varience > 0):
            print("It deals " + str(10 + mag + mp*2 - oppo_def + varience))
            return (10 + mag + mp*2 - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 8:
        print(bcolors.BOLD + bcolors.BLUE + name + " uses Wave!" + bcolors.ENDC)
        if (mag + mp - oppo_def + varience > 0):
            print("It deals " + str(mag + mp - oppo_def + varience))
            return (mag + mp - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 9:
        print(bcolors.BOLD + bcolors.BLUE + name + " uses Waveza!" + bcolors.ENDC)
        if (10 + mag + mp*2 - oppo_def + varience > 0):
            print("It deals " + str(10 + mag + mp*2 - oppo_def + varience))
            return (10 + mag + mp*2 - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 10:
        print(bcolors.BOLD + bcolors.YELLOW + name + " uses Shock!" + bcolors.ENDC)
        if (mag + mp - oppo_def + varience > 0):
            print("It deals " + str(mag + mp - oppo_def + varience))
            return (mag + mp - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 11:
        print(bcolors.BOLD + bcolors.YELLOW + name + " uses Shockeza!" + bcolors.ENDC)
        if (7 + mag + mp*2 - oppo_def + varience > 0):
            print("It deals " + str(7 + mag + mp*2 - oppo_def + varience))
            return (7 + mag + mp*2 - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 12:
        print(bcolors.BOLD + bcolors.BLACK + name + " uses Bash!" + bcolors.ENDC)

        if (atk + mp + 6 - oppo_def + varience > 0):
            print("It deals " + str(atk + mp + 6 - oppo_def + varience))
            return (atk + mp + 6 - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 13:
        print(bcolors.BOLD + bcolors.BLACK + name + " uses Barrage!" + bcolors.ENDC)

        if ((atk + mp - 9 + varience)*4 - oppo_def*2 > 0):
            print("It deals " + str((atk + mp - 9 + varience) - oppo_def*0.5))
            for x in range(0, 3):
                time.sleep(0.2)
                print("Then deals " + str((atk + mp - 9 + varience) - oppo_def * 0.5))
            return ((atk + mp - 9 + varience)*4 - oppo_def*2)
        else:
            print("It deals no damage...")
            return 0
    if id == 14:
        print(bcolors.BOLD + bcolors.PURPLE + name + " uses Blink!" + bcolors.ENDC)

        if (atk + mp - (oppo_def*0.2) + varience > 0):
            print("It deals " + str(atk + mp - (oppo_def*0.2) + varience))
            return (atk + mp - (oppo_def*0.2) + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 15:
        print(bcolors.BOLD + bcolors.PURPLE + name + " uses Blinkeza!" + bcolors.ENDC)
        if ((atk + mp - 9 + varience)*4 - oppo_def*0.4 > 0):
            print("It deals " + str((atk + mp - 9 + varience) - oppo_def * 0.1))
            for x in range(0, 3):
                time.sleep(0.2)
                print("Then deals " + str((atk + mp - 9 + varience) - oppo_def * 0.1))
            return ((atk + mp - 2 + varience) * 4 - oppo_def * 0.4)
        else:
            print("It deals no damage...")
            return 0
    if id == 16:
        print(bcolors.BOLD + bcolors.GREEN + name + " uses Heal!" + bcolors.ENDC)
        return 0
    if id == 17:
        print(bcolors.BOLD + bcolors.DARK + bcolors.GREEN + name + " uses Leaf Drain!" + bcolors.ENDC)

        if (mag + mp - 2 - (oppo_def) + varience > 0):
            print("It deals " + str(mag + mp - 2 - (oppo_def) + varience))
            return (mag + mp - 2 - (oppo_def) + varience)
        else:
            print("It deals no damage...")
    if id == 18:
        print(bcolors.BOLD + bcolors.PURPLE + name + " uses Imbrewence!" + bcolors.ENDC)
        return 0
    if id == 19:
        print(bcolors.BOLD + bcolors.DARK + bcolors.YELLOW + name + " uses Harden!" + bcolors.ENDC)
        return 0
    if id == 20:
        print(bcolors.BOLD + bcolors.DARK + bcolors.YELLOW + name + " uses Hardenza!" + bcolors.ENDC)
        return 0
    if id == 21:
        print(bcolors.BOLD + bcolors.DARK + bcolors.YELLOW + name + " uses Rock Wall!" + bcolors.ENDC)

        if (atk + mp*2 + 16 - oppo_def + varience > 0):
            print("It deals " + str(atk + mp*2 + 16 - oppo_def + varience))
            return (atk + mp*2 + 16 - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 22:
        print(bcolors.BOLD + bcolors.RED + name + " uses Heated Clap!" + bcolors.ENDC)
        if (atk + mp - oppo_def - 2 + varience > 0):
            print("It deals " + str(atk + mp - oppo_def - 2 + varience))
            return (atk + mp - oppo_def - 2 + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 23:
      print(bcolors.BOLD + name + " uses Sword Dance!" + bcolors.ENDC)
      return 0
    if id == 24:
      print(bcolors.BOLD + bcolors.GREEN + name + " uses Illinize!" + bcolors.ENDC)
      return 0
    if id == 25:
      print(bcolors.BOLD + bcolors.DARK + bcolors.GREEN + name + " uses Illinizeza!" + bcolors.ENDC)
      return 0
    if id == 26:
      print(bcolors.BOLD + bcolors.GREEN + name + " uses Herbial Treatment!" + bcolors.ENDC)
      return 0
    if id == 27:
        print(bcolors.BOLD + bcolors.BLACK + name + " uses Fakeout!" + bcolors.ENDC)
        if (atk + mp - oppo_def - 5 + varience > 0):
            print("It deals " + str(atk + mp - oppo_def - 5 + varience))
            return (atk + mp - 5 - oppo_def + varience)
        else:
            print("It deals no damage...")
            return 0
    if id == 28:
        print(bcolors.BOLD + name + " uses Double Kick!" + bcolors.ENDC)
        if ((atk + mp + varience)*2 - oppo_def > 0):
            print("It deals " + str((atk + mp + varience) - oppo_def * 0.5))
            for x in range(0, 1):
                time.sleep(0.2)
                print("Then deals " + str((atk + mp + varience) - oppo_def * 0.5))
            return ((atk + mp + varience) * 2 - oppo_def)
        else:
            print("It deals no damage...")
            return 0
    if id == 29:
        print(bcolors.BOLD + bcolors.DARK + name + " uses Sharp Slice!" + bcolors.ENDC)
        if (atk*1.25 + mp*1.5 - oppo_def + 2 + varience*2 > 0):
            print("It deals " + str(atk*1.25 + mp*1.5 - oppo_def + 2 + varience*2))
            return (atk*1.25 + mp*1.5 - oppo_def + 2 + varience*2)
        else:
            print("It deals no damage...")
            return 0
    if id == 30:
      print(bcolors.BOLD + bcolors.DARK + bcolors.PURPLE + name + " uses Withdraw!" + bcolors.ENDC)
      return 0
    if id == 31:
      print(bcolors.BOLD + bcolors.BLACK + name + " uses Dark Sifin!" + bcolors.ENDC)
      if (mag + mp - oppo_def - 6 + varience > 0):
          print("It deals " + str(mag + mp - oppo_def - 6 + varience))
          return (mag + mp - oppo_def - 6 + varience)
      else:
          print("It deals no damage...")
          return 0
    if id == 32:
      print(bcolors.BOLD + bcolors.BLUE + name + " uses Focus Energy!" + bcolors.ENDC)
      return 0
