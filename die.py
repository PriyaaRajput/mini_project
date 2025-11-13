# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 21:19:30 2025

@author: HP
"""
import random
while True:
    print('='*55)
    print("\n ***Rolling the dice *** ")
    print('='*55)
num=random.randint(1.6)
if num==6:
    print("congrats,you got this",num)
elif num==1:
    print("well tried" )
else:
    print("you got",num)
ch= input("Roll Again?(Y/N)")
if ch in 'nN':
    break
print("thanks for playing game!!!!!")
    