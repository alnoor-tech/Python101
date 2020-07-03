secret_num = "5"
guess = ""
guess_count = 0
guess_limit = 10
out_of_guesses = False
while guess != secret_num and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess a number between 0 - 10: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You are out of guesses! You lose!")
else:
    print("You win!")
