import random
def guess_number():
    while True:
        try:
            guess = int(input("Enter your guess"))
            break
        except:
            print("You have to insert an int number")
    return guess
def check_result(guess, try_num, start, end):
    while True:
        if guess < result:
            start = guess
            try_num += 1
            print(f'Your number is lower than the one I picked. It range between {start} and {end}')
            guess = guess_number()
        elif guess > result:
            end = guess
            try_num += 1
            print(f'Your number is higher than the number I picked. It ranges between {start} and {end}.')
            guess = guess_number()
        else:
            print(f"Correct! You guessed the number {guess} in {try_num} tries.")
            break
def play_again():
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again[0].upper() != 'Y':
        print("Thank for your attend! Hope to see you next time!")
        return False
    return True

game_in = True
while game_in:
    result = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print('\nI have selected a random number between 1 and 100.')
    print('Try to guess what it is!')
    
    start = 0
    end = 100
    try_num = 0

    guess = guess_number()
    check_result(guess, try_num, start , end)

    game_in = play_again()
