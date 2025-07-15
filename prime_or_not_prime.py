# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
primeflag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            primeflag = True
            # break out of loop
            break

    # check if flag is True
    if primeflag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
