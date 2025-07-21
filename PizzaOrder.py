print("Welcome!! to the Pizza Shop: ")
size = input("Enter the size of Pizza (S/M/L): ").upper()
addons = input("Do you need Pepperoni as Addon? (Y/N): ").upper()
extra_cheese = input("Do you need extra Cheese? (Y/N): ").upper()
price = 0
if size == "S":
    price = 150
elif size == "M":
    price = 250
elif size == "L":
    price = 350
else:
    print("Invalid size selected.")
    price = 0
if addons == "Y":
    if size == "S":
        price += 25
    else:
        price += 50
if extra_cheese == "Y":
    price += 20
if price > 0:
    print(f"Your bill is ₹{price}")
