# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 09:20:31 2019

@author: Aarav
"""

#Conditional statement
#nested if
# Check if number is divisible by both 2 and 3 or only 2 or 3
num=int(input("enter number:"))
if num%2==0:
    if num%3==0:
        print("Number is divisible by both 2 and 3")
    else:
        print("Number is divisble by 2 only")
else:
    if num%3==0:
        print("Number is divible by 3 only")
    else:
        print("Number is not divisble by 2 and 3")
    