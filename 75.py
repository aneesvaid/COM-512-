# write a python program to input two list and create a third list containing common elements.
list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

list3 = []

for i in list1:
    if i in list2 and i not in list3:
        list3.append(i)

print("Common elements:", list3)