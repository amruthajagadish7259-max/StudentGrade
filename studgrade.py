import sys

if len(sys.argv) == 7:
    marks_1 = int(sys.argv[1])
    marks_2 = int(sys.argv[2])
    marks_3 = int(sys.argv[3])
    marks_4 = int(sys.argv[4])
    marks_5 = int(sys.argv[5])
else:
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

print("Eng: ",marks_1)
print("Math: ",marks_2)
print("DevOps: ",marks_3)
print("SSW: ",marks_4)
print("SE: ",marks_5)
print("Total Marks:",total)
print("Average: ",avg)
print("Grade: ",grade)
