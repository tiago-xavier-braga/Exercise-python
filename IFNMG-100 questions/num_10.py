salary = float(input("Enter your salary: "))
installment = float(input("Enter your installment "))

percent = salary * 0.3

if percent == installment:
    print("Approved")
else:
    print("Not approved")