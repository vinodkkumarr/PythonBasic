# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 08:43:40 2019

@author: Aarav
"""

# Condtional statement
#if eif statement
#Check for largest of three numbers
firstNumber=float(input("First number: "))
secondNumber=float(input("Second number: "))
thirdNumber=float(input("Third number: "))
if((firstNumber>secondNumber) and (firstNumber>thirdNumber)):
    print ("First number is largest")
elif(secondNumber>thirdNumber):
    print("Second number is largest")
else:
    print("Third number is largest")