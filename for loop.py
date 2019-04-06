# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 09:31:44 2019

@author: Aarav
"""

#Looping statement
#For loop
#Print table
num=int(input("Enter number to print table:"))
for i in range(1,11):
    #print(num*i)
    #print(str(num) + "*" + str(i) + " = " + str(i*num))
    print("{0} * {1} = {2} ".format(i,num,num*i))