from modulo import raiZ
number = int(input("Enter the value...\n"))

if number <= 1:
    print("1")
elif 1 < number <=2:
    print("2")
elif 2 < number <= 3:
    print(raiZ(number))
elif number >  3:
    print(number ** 3)