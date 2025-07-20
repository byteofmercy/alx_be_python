age = int(input("Enter your age: "))

match age:
    case 0:
        print("You're a baby!")
    case 1 | 2:
        print("You're a toddler.")
    case 3 | 4 | 5:
        print("You're in preschool.")
    case _:
        print("You're older than that!")
