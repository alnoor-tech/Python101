lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]


print(friends)
#Extend fubction allows you to take a list and append another list unto the end of it
friends.extend(lucky_number)
print(friends)
#Adding individual objects unto a list (at the end of the list)
friends.append("creed")
print(friends)
#Appends adds something at the end of the list
#If you want to add something at the middle of the list,you use insert function, it takes two parameters
friends.insert(1, "Kelly")
print(friends)
#To remove objects
friends.remove("Kelly")
print(friends)
#clear function removes all list parameters
#friends.clear()
print(friends)  #prints an empty list
#pop function pops an item off the list. It removes the last element in the list
friends.pop()
print(friends)
print(friends.index("Kevin"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Karen", "Toby", "Adam", "Sarah", "Anonymous", "Karen"]
print(friends. count("Karen"))

#sorting in ascending order
friends.sort()
print(friends)

#Sorting in descending order
friends.reverse()
print(friends)

#Making a copy of the list
friends_2 = friends.copy()
print(friends_2)





