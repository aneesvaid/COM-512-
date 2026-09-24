# write a python program to store multiple student records as a list of tuples. each tuples should contain name, roll number, and marks. Display students who cored above 75.
students = [("Anees", 21, 85),
            ("Rahul", 22, 70),
            ("Aman", 23, 90)]

for s in students:
    if s[2] > 75:
        print(s)