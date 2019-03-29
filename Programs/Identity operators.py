print("Identity operators: It only checks if both the operands refer to same object")
a=5
b=6

print ("Value of a = " + str(a))
print ("Value of b = " + str(b))
print("C assigned to A")
c=a
print("Check if c is assigned to a? " + str(a is c))
print("Check if a is assigned to b? " + str(a is b))
print("Check if type of a and b is same?")
print(type(a) is type(b))
x="Vinod"
print(type(a) is not type(x))
print( a is x)

