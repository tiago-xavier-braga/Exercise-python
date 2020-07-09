value = float(input("What's a value...\n"))
if value < 10.00:
    print("Profit: 70%")
elif value >= 10.00 and value < 30.00:
    print("Profit: 50%")
elif value >= 30.00 and value < 50.00:
    print("Profit: 40%")
elif value >= 50.00:
    print("Profit: 30%") 