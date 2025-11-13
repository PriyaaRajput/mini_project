# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 20:24:29 2025

@author: HP
"""
import random
words=['flute','english','rain','hurray','language','java']
word=random.choice(words)
print('Guess te character...')
guesses=' '
Turns=5
while Turns>0:
   failed=0
   for char in word:
         if char in guesses:
            print(char,end='')
         else:
            print("__",end='')
            failed+=1
   print()
   if failed==0:
       print("\n congrats!you won the game")
       print("the word is:",word)        
       break
   guess=input("\n\n guessthe character")
   guesses+=guess
   if guess not in word:
         Turns-=1
         print("Wrong")
         print("you have",Turns,"more guesses")
   if Turns==0:
         print("Better luck next time")
         print("you lose the game")
         print('*'*30)