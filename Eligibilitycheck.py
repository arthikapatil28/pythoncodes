Height=int(input("Enter the Height: "))
if Height>120:
    print("Congrts you are eligible to ride")
    AGE=int(input("Enter the AGE: "))
    if AGE>18:
        print("Cost of ride is 20rs")
    elif AGE in range(12,18):
        print("Cost of ride is 15rs")
    else:
        print("Cost of ride is 10rs")
else:
    print("Opps You cant take a ride")
