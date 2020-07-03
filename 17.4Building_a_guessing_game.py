my_name = "Alnoor"
guess_name = ""
guess_count = 0
guess_limit = 4
out_of_limit = False
while guess_name != my_name and not(out_of_limit):
    if guess_count < guess_limit:
        guess_name = input("Guess my name: ")
        guess_count += 1
    else:
        out_of_limit = True
if out_of_limit:
    print("You lose!")
else:
    print("You win!")

