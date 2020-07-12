A = int(input("Write a number...\n")) 
B = int(input("Write a number...\n")) 
C = int(input("Write a number...\n"))
addition = A + B + C
if addition == 180:
    if A == B == C:
        print("Equilateral")
    elif A != B == C or A == B != C:
        print("Isosceles")
    elif A != B != C:
        print("Scalene")
else:
    print("No, It's not triangle")