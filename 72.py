# write a python program to rotate a list one position to the right.

lst = list(map(int, input("Enter elements: ").split()))

last = lst[-1]

for i in range(len(lst) - 1, 0, -1):
    lst[i] = lst[i - 1]

lst[0] = last

print("List after right rotation:", lst)
