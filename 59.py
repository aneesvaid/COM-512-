# Write a Python program to repeatedly calculate the sum of digits of a number until the result becomes a single digit.
# Example:
# 9875 → 9 + 8 + 7 + 5 = 29 → 2 + 9 = 11 → 1 + 1 = 2


num = int(input("Enter a number: "))

while num > 9:
    sum = 0

    while num > 0:
        sum = sum + num % 10
        num = num // 10

    num = sum

print("Result:", num)