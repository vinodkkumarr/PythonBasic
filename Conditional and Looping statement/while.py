# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:26:53 2019

@author: Aarav
"""

#Looping statement
#While loop
# Print odd numbers of the give range
lower=int(input("Enter lower range: "))
upper=int(input("Enter upper range: "))
if (lower>upper):
    print("Lower range can not be greater than upper range")
else:
    while lower<=upper:
        if (lower%2!=0):
            print(str(lower) + " is an odd number.")
        lower+=1

