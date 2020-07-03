#If statements are used to help a programme make decisions(Conditions: or, and, else if (elif))
is_male = False
is_tall = True
#if is_male or is_tall: #using or operator
#    print("You are male or tall or both")
#else:
#    print("You are neither male not tall")

################### using and

if is_male and is_tall:
    print("Ypu are a tall male")
elif is_male and not(is_tall):#else if
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not a male and not tall")
