price = 1000000
goodCredit = True

if goodCredit:
    print("You need to put down 10%")
    downPayment = 0.1 * price
else:
    print("You need to put down 20%")
    downPayment = 0.2 * price
print(f"Down payment: ${downPayment}")


