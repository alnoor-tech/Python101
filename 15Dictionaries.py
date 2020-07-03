#This is a special structure in python which allows us to store information in key value pairs.
#Can be used to do things like converting Jan to January
#The first step is to give the dictionary a name
#We use curly brackets to create dictionaries in python
#Inside the curly brackets we put key value pairs
#Three letter is the key and the other section is the value
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Nov"]) #also i can access it by:
#print(monthConversions.get("Lob")) #This is the best because if you put something not in the dictionary it returns none instead of an error
#.get also gives us a fallback value that we can get back to if the input is invalid instead of none
print(monthConversions.get("Luv", "Not a valid key!"))
#The keys don't have to be strings, they can also be numbers

