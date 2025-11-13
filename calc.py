# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 19:54:42 2025

@author: HP
"""

print('''
      + ADD
      - SUBTRACT
      * MULTIPLY
      / DIVISION
      ''')
num1=int(input("enter value of num1"))
num2=int(input("enter value of num2"))
operation=input("what operation you want to perform ")
if operation=="+":
  print(num1+num2)
elif(operation=='-'):
  print(num1-num2)    
elif(operation=='*'):
  print(num1*num2)     
elif(operation=='/'):
  print(num1/num2)     
else:
  print("invalid operation")