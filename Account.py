amount=10000
student1 = {
    "checkbalance": 1,
    "withdraw": 2,
    "Deposite Cash": 3,
    "Deposite cheque":4 }
print(student1)
while True:
    student=int(input("Enter the task id u want to perform: "))
    if student == 1:
        print(f"The amount balance is:" ,{amount} )
    elif student == 2:
        withdraw=int(input("Enter the amount to withdraw: "))
        amount=amount-withdraw
        print(f"The amount balannce is:", {amount} )
    elif student == 3:
        cash=int(input("Enter the amount to Depositecash : "))
        amount=amount+cash
        print(f"The amount balannce is:", {amount} )
    elif student == 4:
        cheque=int(input("Enter the amount to Depositecheque: "))
        amount=amount+cheque
        print(f"The amount balannce is:", {amount} )
