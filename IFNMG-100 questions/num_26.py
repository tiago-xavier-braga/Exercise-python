A = int(input("Write a number...\n")) 
B = int(input("Write a number...\n")) 
C = int(input("Write a number...\n"))
addition = A + B + C
if addition == 180:
    if A == 90 or B == 90 or C== 90:
        print("Right triangle")
    elif A > 90 or B > 90 or C > 90:
        print("Obtuse triangle")
    elif A < 90 or B < 90 or C < 90:
        print("Acutangle Triangle")
else:
    print("No, It's not triangle")