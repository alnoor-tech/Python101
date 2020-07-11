#This is meant to catch errors in python
'''
num = int(input("Enter a number: "))
print(num)
'''
#first enter the number and the program runs smoothly
#When you put some random word an error pops up
#In order to allow this program to handle all situations, we can use try except block
#It allows the program to try out a piece of code and if everything runs well then we can account for that


##NEW CODE
'''
try:
    num = int(input("Enter a number: "))
    print(num)
except: #This catches any error under the sun. I mean whatever goes wrong it catches it
    print("Invalid") #This allows handling of the input error
'''
##EXCEPT BLOCKS TO CATCH DIFFERENT TYPES OF ERRORS
try:
    value = 10/0
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError as err:  #Bytha this error can be stored as a valuable err
    print(err)
except ValueError:
    print("Invalid input")

