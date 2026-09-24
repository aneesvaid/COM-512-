# write a python program to store one student data as a tuple: name, roll number, and marks.DISPLAY grade based on marks.
student = ("Anees", 21, 85)

marks = student[2]

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Student:", student)
print("Grade:", grade)