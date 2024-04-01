# input integers
# .split() the 3 integers into seperate variables
# cast the 3 variables to integers
# assign correct variables values from least to greatest
# 'A' will always be less than 'B' and 'B' will always be less than 'C'

integers = input()
a, b, c, = integers.split()
a = int(a)
b = int(b)
c = int(c)

print(f"a: {a} b: {b} c: {c}")
if a >= b:
    a, b = b, a
if b >= c:
    b, c = c, b
if b <= a:
    b, a = a, b
print(f"a: {a} b: {b} c: {c}")

# input the string variable
# determine order of A, B, and C
# create cprrect string
# output string

order = input()
myString = ""

for i in range(len(order)): 
    if order[i] == "A":
        myString += str(a) + " "
    elif order[i] == "B":
        myString += str(b) + " "
    elif: 
        myString += str(c) + " "

print(myString)