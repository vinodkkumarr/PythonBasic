#Variable Names

""" A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
 A variable name must start with a letter or the underscore character
 A variable name cannot start with a number
 A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
 Variable names are case-sensitive (age, Age and AGE are three different variables) """


#Remember that variables are case-sensitive

x = 4 # x is of type int
x = "Vinod" # x is now of type str
print(x)

#Output Variables

# The Python print statement is often used to output variables.

# To combine both text and a variable, Python uses the + character:

x="Vinod K"
print("My name is: " + x)

x="My name is "
y="Vinod"

print(x + y)

# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)
