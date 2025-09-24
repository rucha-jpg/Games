import random
import game_data

input("Let's start! Press Enter.")

play_again = True
while play_again:
    score = 0
    x = random.randint(0, 49)
    to_continue = True
    while to_continue:
        y = random.randint(0, 49)
        if y == x:
            y = random.randint(0, 49)

        answer_a = game_data.data[x]['follower_count']
        answer_b = game_data.data[y]['follower_count']
        highest = ""
        if answer_b > answer_a:
            highest = "b"
        elif answer_a > answer_b:
            highest = "a"

        print("COMPARE:")
        print(f"A: {game_data.data[x]['name']}, a {game_data.data[x]['description']}, from {game_data.data[x]['country']}")
        print("VS")
        print(f"B: {game_data.data[y]['name']}, a {game_data.data[y]['description']}, from {game_data.data[y]['country']}")

        guess = input("Who has the highest followers? A or B? ").lower()

        if guess == highest:
            print("Right!")
            score += 1
            print(f"Current score: {score}")
            input("Press enter to continue.")
            print("\n" * 30)
            if guess == "a":
                x = x
            elif guess == "b":
                x = y
            to_continue = True
        else:
            print("\n"*30)
            print("Wrong!")
            print(f"Your final score is: {score}")
            to_continue = False
            play = input("Do you want to play again? Y or N ").lower()
            if play == "n":
                play_again = False