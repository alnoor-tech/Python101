#Reading files from outside python
#You use modes such as "r"=read, "W"=Write, "a"=Append(You cannot modify any ifnormation in the file but you can add
#"r+"=This means read and write.
#Store the opened file(open("H_Tools.txt", "r")) inside a variable for it to be executed
#Whenever you open a file just make sure you close the file as well
#First, check whether the file is readable using readable function
Hacking_Tools = open("H_Tools.txt", "r")
print(Hacking_Tools.readable())  #Returns a boolean value, readable(True), if it was in "W" mode it would return false
#print(Hacking_Tools.read()) #This helps you see the contents of the file in the console
#print(Hacking_Tools.readline()) #This reads the first line in the file, if you want to read the second line then you copy the lineof code
print(Hacking_Tools.readlines()) #Puts each of the line in the file in an array. You disable .read to have this work
print(Hacking_Tools.readlines()[1]) #Allow you access any given line in the text
Hacking_Tools.close()

