age = int(input("What's you age ?\n"))

if age <= 10:
    print("R$ 30,00")
elif age > 10 and age <= 29:
    print("R$ 60,00")
elif age > 29 and age <= 45:
    print("R$ 120,00")
elif age > 45 and age <= 59:
    print("R$ 150,00")
elif age < 59 and age <= 65:
    print("R$ 250,00") 
else :
    print("R$ 400,00")