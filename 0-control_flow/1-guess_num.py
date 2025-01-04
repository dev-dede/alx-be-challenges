import random
secret_number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))
while guess != secret_number:
    match guess:
        case _ if guess < secret_number:
            guess = int(input("Nope, your guess is a bit low. Give it another shot! "))
        case _ if guess > secret_number:
            guess = int(input("Nope, your guess is a bit high. Give it another shot! "))
print("Congratulations, you guessed it!")