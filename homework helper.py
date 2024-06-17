final = int(input("final grade"))

midterm = int(input("midterm grade"))

homework = int(input("homework grade"))


overall = (final * 30/100) + (final * 40/100) + (homework * 30/100)

print(f"your grade is {overall}")


if final > midterm and homework > midterm:
    print("next time spend more time on your final")
elif final <= midterm:
    print("next time spend more time on your homework")
else:
    print("next time spend more time on your midterm")


