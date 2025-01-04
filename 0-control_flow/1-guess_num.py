import random

#Main game loop
while True:
    secret_number = random.randint(1, 10)
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))

    #Loop until user gets the guess correct
    while guess != secret_number:
        match guess:
            case _ if guess < secret_number:
                guess = int(input("Nope, your guess is a bit low. Give it another shot! "))
            case _ if guess > secret_number:
                guess = int(input("Nope, your guess is a bit high. Give it another shot! "))
    print("Congratulations, you guessed it!")

    #Ask player if they want to play again
    play_again = input("Play again? (yes/no) ").lower()
    if play_again == "yes":
        print("....New game starts!")
    else:
        print("Thanks for playing! Goodbye!")
        break
