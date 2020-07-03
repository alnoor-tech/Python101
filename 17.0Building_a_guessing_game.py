#Buillding basic guessing game using all coding structures that we have learned so far
#We have a secret word that we will store in the programme and the user can interract with the program and try to guess the secret word
#We want the user to keep on guessing and getting different responses until they guess the secret word
secret_word = "giraffe" #a variable for our secret word
guess = "" #this variable containing an empty string will store all the user's guesses
#Let's now prompt the user to input a secret word
#We want them to enter a secret word and if they wron we want to prompt them to enter it again
while guess != secret_word:
    guess = input("Enter guess: ")
print("You win")
