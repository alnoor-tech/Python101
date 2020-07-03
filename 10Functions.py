#Function is a collection of code that performs a specific task
#Help organize and break your code into different little chuncks that do different things
#Let create a function that says his to the user
#key word def is used and then the name of the function
#Parameter is a piece of information that we give to the function
#Parameters are entered inside the bracked of the def name

#def say_hi():    #This means that all the code that comes below this line is inside our function
#    name = input("Hi, what is your name: ")
#    print("Hello " + name + "!")
#say_hi() #This is calling the function

#def sayhi(name):
#    print("Hello " + name +  "!")
#sayhi("Mike") #mike was passed on here
#sayhi("Steve")

#You can put as many parameters as you may like
#def say_hi(name, age):
#    print("Hello " + name + "! You are " + age + " years old.")
#say_hi("Mike", "26")
#say_hi("Steve", "28")

def say_hi(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old.")
say_hi("Mike", 26)
say_hi("Steve", 28)



