def max_num(num1, num2, num3): #We are passing in three numbers and the function will return the largest of the three
   if num1 >= num2 and num1 >= num3: #comparison operators /double == means equal and != means not equal
       return num1
   elif num2 >= num1 and num2 >= num3:
       return num2
   else:
       return num3
print(max_num(4, 18, 2))
