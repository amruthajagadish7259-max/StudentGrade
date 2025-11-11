import sys

if len(sys.argv) == 7:
    name = sys.argv[1]
    marks_1 = float(sys.argv[2])
    marks_2 = float(sys.argv[3])
    marks_3 = float(sys.argv[4])
    marks_4 = float(sys.argv[5])
    marks_5 = float(sys.argv[6])
else:
    name = "xyz"
    marks_1 = 50
    marks_2 = 70
    marks_3 = 85
    marks_4 = 90
    marks_5 = 85

total = marks_1 + marks_2 + marks_3 + marks_4 + marks_5
avg = total / 5

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
elif avg >= 50:
    grade = "E"
elif avg >= 40:
    grade = "F"
else:
    grade = "Fail"

print(f"File: {name}")
print(f"Eng: {marks_1}")
print(f"Math: {marks_2}")
print(f"DevOps: {marks_3}")
print(f"SSW: {marks_4}")
print(f"SE: {marks_5}")
print(f"Total Marks: {total}")
print(f"Average: {avg}")
print(f"Grade: {grade}")
