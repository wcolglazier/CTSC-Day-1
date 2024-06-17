Age = int(input("Enter your age: "))

if Age >= 17:
    test = input("Have you passed a drivers test? (yes/no) ")
    if test == 'yes' and Age <= 80:
        print("You can drive!!")

    else:
        print("You can't drive sorry")
else:
    print("You can't drive sorry")



