num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
#The above is a grid, of lists within a list (4 rows and 3 columns)

]
#Accessing elements inside the 2-dimensional list
print(num_grid[0][0])  #   print(num_grid[row][col])
print(num_grid[1][2])

#Nested for loop is a for loop inside a for loop. We can use it to print all the elements inside the array
#Using for loop to print all the elements in the 2d-Array
for row in num_grid:
    print(row) #this prints all the rows in the num_grid
#Accessing each of the individual attributes inside each of the array elements
for row in num_grid:
    for col in row:
        print(col)



