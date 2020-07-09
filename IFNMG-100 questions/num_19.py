age = int(input("What's you age ?\n"))

if age < 18:
    print("Minor")
elif age > 18 and age < 65:
    print("Majority")
else:
    print("Aged")