print("Next year time like now,\nI will be gearing for NIS training.")
#Backslash n \n introduces another line below the first section of the string
#Backslash quotation marks prints out a quotation mark
print("I love her\" so much!")
#To print out a normal backslash in a code
print("Ya Allah\habibi")

#CREATING A STRING VARIABLE
phrase = "I love Sarah\habibi"
print(phrase)
#CONCANTENATION - Taking a string and appending it in another string
print(phrase + " and is cool and i like it that way")

#Using of special things called functions FUNCTIONS FUNCTIONS FUCNTIONS - a block of code that w e can run to perform a specific operation
print(phrase.lower()) #converts phrase into lower case
print(phrase.upper()) #converts phrase into upper case
#Using function to check whether its true or false...you use isupper() or islower()
print(phrase.isupper())
print(phrase.islower())
#Using functions in combination with each other
print(phrase.upper().isupper())
print(phrase.lower().islower())
#Figuring out the length of a string
print(len(phrase))
#Grabbing a single character from a string/A string get indexed starting with zero
print(phrase[0])
#The index function- tells us where a specific character or a string is located inside of a string
print(phrase.index("o"))
print(phrase.index("love"))  #If you put a letter that is not in the string then it will return an error
#Replace function
print(phrase.replace("habibi", "kajuju"))








