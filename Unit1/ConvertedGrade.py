# input
grade = int(input("Enter your grade: "))
grade17 = 0

# if statement
if grade >= 28:
    grade17 = 7
elif grade >=23:
    grade17 = 6
elif grade >= 19:
    grade17 = 5
elif grade >= 15:
    grade17 = 4
elif grade >= 10:
    grade17 = 3
elif grade >= 6:
    grade17 = 2
elif grade >= 1:
    grade17 = 1
else:
    grade17 = 0

print("1-7 grade: ", grade17)