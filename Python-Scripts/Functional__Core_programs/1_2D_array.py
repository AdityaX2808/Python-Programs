#Declaring the dimensions of the matrix
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

#Matrix implementation
matrix = [[int(input()) for _ in range(columns)] for _ in range(rows)]

#Printing the matrix
for rows in matrix:
    print(rows)