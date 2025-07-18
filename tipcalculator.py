print("Welcome to tip calculator ")
total=int(input("what was the total Bill?: "))
tip=int(input("How much tip you would like to give 10 20 30: "))
people=int(input("How many people to split the bill: "))
sub=total-tip
bill=sub//people
print(f"Your Total bill was: {total}rs \nReducing the tip of amount {tip}rs will give: {sub}rs")
print(f"Each person need to pay {bill}rs")
