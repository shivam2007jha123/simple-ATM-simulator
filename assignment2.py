marks1=float(input("enter your marks 1:"))
marks2=float(input("enter your marks 2:"))
marks3=float(input("enter your marks 3:"))
marks4=float(input("enter your marks 4:"))
marks5=float(input("enter your marks 5:"))
average=(marks1+marks2+marks3 + marks4+marks5)/5
if average>=90:
    grade="A"
elif average>=80:
    grade="B"
elif average>=70:
    grade="C"
elif average>=60:
    grade="D"
elif average>=50:
    grade="E"
elif average>=40:
    grade="F"
else:
    grade="F"
print("Average",":",average)
print("grade",":",grade)