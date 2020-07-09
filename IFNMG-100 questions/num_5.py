number_one = int(input("Write s number: "))
number_two = int(input("Write s number: "))

result = number_one + number_two

if result > 20:
    result += 8
    print(result)
elif result < 20:
    result -= 5;
    print(result)