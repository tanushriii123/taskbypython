try:
    age = int(input("Enter your age: "))

    if age < 10 or age > 99:
        print("Please enter a two-digit integer only.")

    elif age < 13:
        print("Childrens are not eligible to vote.")

    elif age <= 18:
        print("You are eligible to vote.")


except ValueError:
    print("Please enter an integer only.")