A = int(input("Write a number: "))
B = int(input("Write a number: "))
C = int(input("Write a number: "))
D = int(input("Write a number: "))
list = [A, B, C, D]
i = 0
while i <= 3:
    if list[i] >= A and list[i] >= B and list[i] >= C and list[i] >= D:
        bigger = list[i]
    elif list[i] <= A and list[i] <= B and list[i] <= C and list[i] <= D:
        smaller = list[i]
    i += 1
print("Bigger :", bigger, "smaller: ", smaller)