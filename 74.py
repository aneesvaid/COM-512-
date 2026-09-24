# Write a Python program to count how many times a particular element appears in a list.

numbers = [10,20,10,30,10,40,20]
search = int(input("enter number to count: "))
count = 0;
for  num in numbers:
   if num == search:
       count = count + 1
       print("Frequency:") 