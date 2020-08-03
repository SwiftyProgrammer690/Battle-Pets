#Importing Stuff
import sys
import time
import random
from time import sleep
from random import randint
from sys import exit
from random import choice



#Game Data
user = input('Welcome, ..... Are you a new player, Yes or No ')
if user=="Yes":
  print('Hello New Player, You might be wondering what the rules are, well let me explain, You will be given 2 questions if you pick the right one you are safe... but if you pick the wrong one, you will be fighting a monster Lv. 5, ATKDMG is 17hp., HP is 30. Your Stas are Lv. 4,ATKDMG is 12hp., HP is 25.... but dont worry, you always have a HEALING POTION *INTENSE MUSIC*, you can use this potion only if you answer the potion question Correctly if you do not then chances are youll lose the game, and you have only one potion in a game. Wel that is it oh and you have only ten questions or batles or both and if you survive ten rounds you win the game, now refresh your browser and press No and enjoy the game. CODED BY @PYTHONSWARIT')

else:
  question = input('Is Tmobile the largest 5G network in America, True or False ')
  if question=="True":
    print('Good Job, you are moving on')
    question2 = input('Is India the 7th largest country in the world, True or False ')
  else:
    print('You got it wrong unfortunatly')
    Monster_question = input('What to use? Attack or potion')
    if Monster_question=="Attack":
     print('You did 12 damage, The monster has 28hp')
     print('The monster attacks you, you have 18hp.')
     Monster_question2 = input('What to use? Attack or potion')
     if Monster_question2=="Attack":
       print("You did 12 DMG, the monster has 16hp.")
       print('The monster attacks you, you have 1hp. left')
     #Easter egg for shield 
     else:
       Potion_question2 = input('Which planet is close to earth, Mercury or Venus')
       if Potion_question2=="Mercury":
        print('You are correct, you healed 12hp, you have 13hp. and you have a 6- resistiance meaning when monster attaks you the damage will turn into 11 damage.')
        #Easter egg for sheild ends
        print('The monster attacks, POWER PLAY, RESITANCE, 2hp. remaining')
        #Easter egg for attack DMG
        print("Since you already haave used your potion, you attacked, The monster has 12DMG, the monster has only 4 hp left")
        sleep(10)
        print("POWER PLAY")
        print('INSTANT KILL')
        #Easter egg for attack DMG ends

    else:
      Potion_question = input('If you were to travel east from New York, where would you land, Europe, or Africa')
      if Potion_question=='Africa':
        print('Well you wasted your only potion, and its pretty obvious so:')
        sys.exit("GAME OVER")
      else:
        print('Good job but you cant use it now because your still at full health, but the next time you enter potion then you will automattilcly get the sheild')
        print('Tje monsyter attacks you, you have 18 hp. remaining')
        #Easter egg for give up
        sleep(3)
        print("The monster gave up beacause he gave up")
        #Easter egg for give up ends
      
