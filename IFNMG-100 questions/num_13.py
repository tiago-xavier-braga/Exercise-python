A = int(input("Write a number: "))
B = int(input("Write a number: "))
C = int(input("Write a number: "))
set = [A, B, C]
i = 0
while i <= 2:
    if set[i] >= A and set[i] >= B and set[i] >= C:
        bigger = set[i]
    elif set[i] <= A and set[i] <= B and set[i] <= C:
        smaller = set[i]
    elif set[i]!= bigger and set[i] != smaller:
        medium = set[i]    
    i += 1
print(bigger, medium, smaller)  