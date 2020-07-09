from modulo import raiZ, quad
A = int(input("Write a number: "))
B = int(input("Write a number: "))

if A > B:
    print(quad(B))
    print(raiZ(A))
elif A < B:
    print(quad(A))
    print(raiZ(B))
