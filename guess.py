import random

number_of_guesses = 0

number_to_be__guessed = random.randint(1, 100)

while number_of_guesses < 5:
    guess = int(input("guess a number between 1 to 100: "))

    if guess < number_to_be__guessed:
        print("too low")
    else:
        if guess > number_to_be__guessed:
            print("too high")
        else:
            if guess == number_to_be__guessed:
                print("you are right")
                break

    number_of_guesses += 1
else:
    print("you are a failure try again later the number is:", number_to_be__guessed)


