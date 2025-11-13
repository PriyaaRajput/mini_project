# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:03:26 2025

@author: HP
"""


import random
emojis={'r':'🪨','p':'📃','s':'✂'}
choice=('r','p','s')
while True:
   ch=input("do u want to play a game:").lower()
   if ch=='y':
    cmp_chose= random.choice(choice)
    you_chose=input("Rock,Paper,Scissors?(r/p/s):").lower()
    if you_chose not in choice:
        print("Invalid choice")
        continue
    print(f"you chose{emojis[you_chose]}")
    print(f"computer chose{emojis[cmp_chose]}")
    if(you_chose==cmp_chose):
        print("Tie!!")
    elif(
            (you_chose =='r' and cmp_chose=='s') or   
            (you_chose =='s' and cmp_chose=='p') or   
            (you_chose =='p' and cmp_chose=='r')):  
        print("you won the game")
    else:
         print ("you lose the game")

   elif ch not in 'y/n':
        print("Invalid choice")
        print("Please enter a valid choice")
   elif ch in 'n':
        print("Let's play next time")
        break
    
         