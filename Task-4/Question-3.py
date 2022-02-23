# Program to make a 2-dimensional lst that contains represents a table of records
a=[[1, 'Abc', 90],
   [2, 'Ded', 95],
   [3, 'Ghi', 85]]
print("{:<10} {:<10} {:<10}" .format('Roll no', 'Student name', 'Marks'))
for i in range(len(a)):
    print()
    for j in range(3):
     print(a[i][j], end = " "*10)
print("\nThe second row from the data is")
for i in range(3):
    print( a[1][i], end=" "*10)
print()
