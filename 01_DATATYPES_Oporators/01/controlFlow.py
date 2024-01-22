# Control Flow, Aziah Hill, v0.0
# DECLARATIONS

favColor = "Purple"
luckyNumber = "5"
myGPA = 3.6
myAge = 16
pineappleOnPizza = True

# # if Statements - Check for a condition to be True/False, do something
# if favColor == "Purple":
#     print("I like your style.")

# if luckyNumber > 28:
#     print("Bring bumbers for a winner!")

# # if-else Statement -- Check for a condition, do something for True/False
# if myGPA >= 3.0:
#     print("Congragulations on making the honor roll!")
# else:
#     print("Better luck next year. Try to study more!")

# if pineappleOnPizza == True:
#     print("You believe in the right thing buddy")

# # if - elif - else Statement -- Checks for multiple conditions
# if myAge < 18:
#     print("Congratulations, you aint old!")
# elif myAge > 50:
#     print("Congratulations, you have earned a bonus of $1000!")
# else:
#     print("You are not old enough for the bonus.")
# #1 if, 1 else, any number of elif allowed.

# # Nested if - elif - else Statements
# if myAge > 15:
#     print("You are eligible for a license!")
#     if myGPA >= 3.5:
#         print("You qualify for a new car!")
#     elif myGPA > 2.0:
#         print("you qualify for $500 off a car!")
#     else:
#         print("You get nothing!")
# else:
#     print("You are not yet old enough to drive")

# # When doing if - elif - else statements, check for the highest values first!!!!
# if myGPA > 1.5:
#     print("You are in danger of failing for the year.")
# elif myGPA > 2.0:
#     print("You are on track to graduate.")
# elif myGPA > 3.0:
#     print("You qualify for some scholarship money!")
# elif myGPA > 3.99:
#     print("You qualify for Bright Futures 100 percent scholarship!")
# else:
#     print("GPA nwas not calculate. Please try again.")

# # While Loop -- Think "MUSICAL CHAIRS" -- Used when you do NOT know how many interactions you need.
# # iteration = one complete trip through a loop
x = 0
while x < 100: 
    print(f"X is currently equal to {x}")
    x += 1
while x < 100: 
    print(f"X is currently equal to {x}")
    x += 1

# for Loop -- think 'Go Fish', used when you know number of iterations needed.
for i in range(10): # i = iterable variable
    print(i)

print("EVEN OR ODD LOOP!")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is even")
    else:
        print("That number is odd!")
    


    # () Parenthesis
    # [] Square Brakcets
    # <> Angle Brakcets
    # {} Braces

    