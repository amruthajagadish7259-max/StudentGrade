import sys
if len(sys.argv)==5:
     marks_1=sys.argv[0]
     marks_2=sys.argv[1]
     marks_3=sys.argv[2]
     marks_4=sys.argv[3]
     marks_5=sys.argv[4]


else:
     marks_1=50
     marks_2=70
     marks_3=85
     marks_4=90
     marks_5=85

     
     total=marks_1+marks_2+marks_3+marks_4+marks_5
     avg=total/5

print(f"English:{marks_1}")
print(f"DM:{marks_2}")
print(f"Devops:{marks_3}")
print(f"SSW:{marks_4}")
print(f"SE:{marks_5}")


print(f"The total marks:{total}")
print(f"Average:{avg}")
     
