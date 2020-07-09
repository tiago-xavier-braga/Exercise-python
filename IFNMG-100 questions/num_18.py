A = int(input("Write a number: "))

if A > 0 and A <= 500:
    print("None")
elif A >= 501 and A <= 1000:
    print("30%")
elif A >= 1001 and A <= 3000:
    print("40%")
elif A >= 3001:
    print("50%")