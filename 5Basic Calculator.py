num_1 = input("Enter a number: ")
num_2 = input("Enter another number: ")
#Note that whatever input is got from the user is converted into a string by default.
#Therefore, we need to convert the strings that we get from a user into numbers using either int
#However, int won't work for decimals. Float is just basically a number that has decimals.
#sum = int(num_1) + int(num_2)
sum = float(num_1) + float(num_2)
print(sum)
