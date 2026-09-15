# write a python program to print a square pattern of stars for n rows and n coloumns.
# * * * *
# * * * *
# * * * * 
# * * * *

n = int(input("Enter number of rows and columns: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()