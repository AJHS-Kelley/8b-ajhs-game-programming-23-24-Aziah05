# Data Types and Operaters, Aziah Hill, v0.3s

# Variable Rules
# CANNOT START WITH A NUMBER!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLES NAME SHOULD DESCRIBE THE DATA.
# snake_case variables use _ to separate words, all lower case.
# camelCase variables do not use spaces, 1st word lower, rest upper.

# String Literal Examples
playerName = "Folks"
empytString = ""
spaceString = " "
spaceString = "Eat chicken"
bossName = "Tracer"

# Integer Data Types
health = 150
extraLives = 3
armor = 50
dph = 15

# Floating Point Data Types
lapTime = 3.5
velocity = 2.0
pi = 3.1415678

# Boolean Data Types
isFireType =  False
weaponEquipped = True
pvpEnabled = False

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(4 + -2) # Addition
print(1 - 26) # Subtraction
print(2 * -2) # Multiplication
print(4 / -2) # Division
print(4 ** 5) # Exponents
print(16 % 2) # Modules -- Divides, then returns remainder, most commonly used to deterine even/odd

# Comparison Operators
# Evfaluate the expression then return True or False
print(7 > 3) # Greater Than
print(9 >= -2) # Greater Than or Equal To
print(-1 < -3) #Less Than
print(4 <= -4) #Less Than or Equal To
print(5 == 1) # Is Equal To
print(-10 != 3) # Not Equal To

# Assignment Operators
myVariabe = "myValue" # Assign Variable on the eft value on the right, throw out any current value
myOtherVariable = (11 + 6)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignment Operator -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print(3 < 5 and 4 > 3) # AND requires ALL expressions to be True.
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "Purple" and temp == -5)
# When writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires ONE expression to be True.
print(5 > 2 or 2 < -2)
print(3!= 3 or 5 == 5)

# AND OR Combined
print("Line 81")
print(3 > 2 and 4 < 3 or 5 != 7)
# print(True and False or True)

# NOT Logical Operator
print(not (3 > 2))
print(not (not (not (5!=3))))