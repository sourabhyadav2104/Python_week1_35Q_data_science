## Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.

## Taking input from user for rows and columns!!
number_rows = int(input("Enter the number of rows: "))
number_columns = int(input("Enter the number of columns: "))

# Create a 2-dimensional array of zeros with dimensions number_rows by number_columns..
array = [[0 for j in range(number_columns)] for i in range(number_rows)]

# Fill the array with the values of i*j
for i in range(number_rows):
    for j in range(number_columns):
        array[i][j] = i*j

# print the array
for row in array:
    print(row)
