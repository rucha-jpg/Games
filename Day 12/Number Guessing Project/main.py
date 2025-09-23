import random

answer = random.randint(0, 100)
print("Welcome to the number guessing game!")
print("Guess a number between 0 to 100")
play_again = True

while play_again:
    difficulty = input("Choose a difficulty level: Easy or Hard ").lower()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5

    def num_attempts():
        print(f"You have {attempts} attempts left.")

    for i in range(0, attempts):
        num_of_attempts = True

    while num_of_attempts:
        guess = int(input("Enter a number: "))
        if guess > answer:
            print("Too High")
            attempts -= 1
            num_attempts()
        elif guess < answer:
            print("Too Low")
            attempts -= 1
            num_attempts()
        elif guess == answer:
            print("You guessed it!")
            num_of_attempts = False

        if attempts == 0:
            num_of_attempts = False
            print(f"It was {answer}. You idiot!")

    if input("Do you want to play again?: y or n ").lower() == "n":
        print("Goodbye")
        play_again = False