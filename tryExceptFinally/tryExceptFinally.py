# This is a method for testing code and preventing crashes
# try -- except -- else

try: # the code in this block is always executed
    myVariable = 1
    print(myVariable)
except NameError: # This code will run if there is an error
    print("There is an incorrect variable name in your code.")
except: # this code will run if there is an error (exception)
    print("Uh Ohhh, Something has gone wrong!")
else: # This code runs if there are no errors
    print("Code exected correctly with no exceptions")
finally: # this code alwaus runs
    print("I'll be back.\n")
