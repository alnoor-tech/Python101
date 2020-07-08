print("Hello, welcome to world facts quiz!")
ans = input("Are you ready to play (yes/no): ")
score = 0
total_q = 6
if ans.lower() == "yes":
    print("Try to answer all the ten questions without using google! Challenge yourself!")
    ans = input("1. Which is the best country in the world for Safari? ")
    if ans.lower() == "kenya":
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The answer is Kenya")

    ans = input("2. Between tea and coffee, which is Kenyan's favorite beverage? ")
    if ans.lower() == "tea":
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The correct answer is tea")
    ans = input("3. Which is home country to Maasai people? ")
    if ans.lower() == "kenya":
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Kenya")
    ans = input("4. Which island in kenya is car-free? Residents walk, take a boat, or use donkeys to transport items. ")
    if ans.lower() == "lamu":
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Lamu")
    ans = input("5. Which country is named after a mountain? ")
    if ans.lower() == "kenya":
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Kenya")
    ans = input("6. Kenya has how many official languages? ")
    if ans.lower() == "2":
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The correct answer is 2: English and Kiswahili")
