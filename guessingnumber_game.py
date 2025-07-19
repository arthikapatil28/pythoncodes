import random
def nummber_guessing_game():
    secret=random.randint(1,100)
    guess=None
    print('''iam picking a number from 1 to 100 \nPlease pick a number and guess the crt number ''')
    while guess !=secret:
        guess=int(input("Enter the number i picked:"))
        if (guess < secret):
            print('to low guess a bigger:')
        elif (guess > secret):
            print("to High guess a lower:")
        else:
            print("congratualations you guessed right!")

nummber_guessing_game()
