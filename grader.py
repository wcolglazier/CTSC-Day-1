test_grade = int(input("Test grade: "))

homework_grade = int(input("Test grade: "))

# test is 80% of the grade homework is 20% of the grade

final_grade = (test_grade * 80/100) + (homework_grade * 20/100)

if final_grade >= 80:
    print("Good job you got an A")
elif final_grade >= 70:
    print("Good job you got an B")
elif final_grade >= 60:
    print(" You got a C")
else:
    print("You did not pass")