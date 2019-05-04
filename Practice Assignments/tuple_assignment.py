# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:58:22 2019

@author: Aarav
"""

#1. Write a Python program to create a tuple. 
x=2,3,4
print(x)
#2. Write a Python program to create a tuple with different data types. 
x=2,3,"vinod",6
print(x)

#3. Write a Python program to create a tuple with numbers and print one item. 
x=1,2,3
x=1,
print(x)

#4. Write a Python program to unpack a tuple in several variables. 
x=1,2,3
a,b,c=x
print(a)
print(b)
print(c)

#5. Write a Python program to add an item in a tuple. 
x=(1,2,3)
lst=list(x)
lst.append(4)
x=tuple(lst)
print(x)


#6. Write a Python program to convert a tuple to a string. 
tpl=("a","b","c")
str=''
str=str.join(tpl)
print(str)

#7. Write a Python program to get the 4th element and 4th element from last of a tuple. 
tpl=(1,2,3,4,5,6)
print("Fourth element of the tuple: " , tpl[3])
print("Fourth element from the last of the tuple: ", tpl[-4])

#8. Write a Python program to create the colon of a tuple. 
tpl=('Vinod',2,[],True)
tpl[2].append(10)
print(tpl)



#9. Write a Python program to find the repeated items of a tuple
tpl=(1,5,3,4,3,5)
num=int(input("Enter number to find if item is repeated in tuple:"))
cnt=tpl.count(num)
if cnt>1:
    print(num, " is repeated", cnt , " times in tuple" , tpl)
else:
    print(num, " is not repeated in tuple" , tpl)



#10. Write a Python program to check whether an element exists within a tuple. 

tpl=(1,5,3,4,3,5)
num=int(input("Enter number to find if item exist in tuple:"))
if num in tpl:
    print(num , " exist in tupple - > ", tpl)
else:
    print(num, " does not exist in tuple - > ", tpl)


# 11. Write a Python program to convert a list to a tuple. 
lst=["a","b","b","c"]
tpl=tuple(lst)
print(tpl)



# 12. Write a Python program to remove an item from a tuple
tpl=(1,2,3,4,5,"hello")
print(tpl)
lst=[]
for n in tpl:
    lst.append(n)
lst.remove(1)
print(lst)
tpl=tuple(lst)
print(tpl)

# 13. Write a Python program to slice a tuple
#tuple[start:stop:step]

tpl=(1,2,3,4,5)
_slice=tpl[3:5]
print(_slice)
_slice=tpl[:3]
print(_slice)
_slice=tpl[1:]
print(_slice)
_slice=tpl[:]
print(_slice)
_slice=tpl[::3]
print(_slice)
_slice=tpl[3::]
print(_slice)
tpl=tuple("Hello world")
print(tpl)
#tuple[start:stop:step]
_slice=tpl[1:4:2]
print(_slice)
_slice=tpl[::4]
print(_slice)

_slice=tpl[7:2:-4]
print(_slice)

'''
#14. Write a Python program to find the index of an item of a tuple.
tpl=("My name is vinod kumar")
idx=tpl.index("is")
print(idx)
idx=tpl.index("n",2)
print(idx)
idx=tpl.index("pan")
print(idx)
'''
# 15. Write a Python program to find the length of a tuple.
tpl=("Hello, how are you?") 
l=len(tpl)
print(l)

# 16. Write a Python program to convert a tuple to a dictionary. 
tpl=(1,2,3,4,5,"A",5,"b")


# 17. Write a Python program to unzip a list of tuples into individual lists. 
tpl=((1,2),(3,4),("a","b"),(1,"a","c"))
for x in tpl:
    lst=list(x)
    print(lst)

def _rev(ls):
    lst=[]
    cnt=len(ls)-1
    for i in range(cnt,-1,-1):
        lst.append(ls[i])
    return lst
# 18. Write a Python program to reverse a tuple. 
tpl=(1,2,3,4,5,6)
lst=[]
for i in tpl:
    lst.append(i)
tpl=tuple(_rev(lst))
print(tpl)


#20. Write a Python program to print a tuple with string formatting. 
tpl=(100,200,300)
print("This is a tuple {}".format(tpl))

# 21. Write a Python program to replace last value of tuples in a list

lst=[(10, 20, 40), (40, 50, 10,90), (70, 80, 10)]
print("Original List :  {}".format(lst))

def removewithintupleoflist(lst):    
    lst1=[]
    for x in lst:
        l=list(x)
        l.insert(len(x)-1,100)
        l.pop()
        lst1.append(l)
    lst=lst1
    for j in range(len(lst)):
        lst[j]=tuple(lst[j])
    return lst
       
print("Modified last item of tuple of a list :  {}".format(removewithintupleoflist(lst)))


    
#22. Write a Python program to remove an empty tuple(s) from a list of tuples. 
#Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']


lst= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("Original list : {}". format(lst))

def removeemptytuple(lst):
    lst1=[]
    t=('',)
    for x in lst:
        if(len(x))!=0:
            lst1.append(x)
        else:
            lst1.append(t)
    return lst1

  
print("Modified list : {}". format(removeemptytuple(lst)))



#23. Write a Python program to sort a tuple by its float element. 
#Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


lst=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
lst.sort(reverse=True)
print(lst)


#24. Write a Python program to count the elements in a list until an element is a tuple.

lst=['a','b',{'a':1,'b':2,'c':3},('a','b')]
for x in lst:
    if ('tuple' in x):
        break
    else:
        print(len(x))
    
lst.clear()





