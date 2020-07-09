number = int(input("Write a number: "))

if number >= 0:
    number *= 0.5
    print(number)
elif number < 0:
    number *= number
    print(number)