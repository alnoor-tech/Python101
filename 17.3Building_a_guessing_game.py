my_age = "26"
guess_age = ""
guess_age_count = 0
guess_age_limit = 5
out_of_limit = False
lower_limit = "20"
upper_limit = "30"
out_of_range = False
while guess_age != my_age and not(out_of_limit):
    if guess_age_count < guess_age_limit:
        guess_age = input("Guess my age. Its between 20 and 30: ")
        guess_age_count += 1
    else:
        out_of_limit = True
if out_of_limit:
    print("You lose!")
else:
    print("You win!")