import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
input("Let's start! Press enter.")
should_loop = True
while should_loop:
    player_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    computer_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    number_of_comp_cards = random.randint(0, 3)
    for i in range(0, number_of_comp_cards):
        computer_cards.append(random.randint(0, 12))


    sum_player = sum(player_cards)
    sum_comp = sum(computer_cards)

    def compare():
        if sum_player > 21 and sum_comp > 21:
            print("You both lose!")
        elif sum_player > 21:
            print("YOU LOSE!")
        elif sum_comp > 21:
            print("Computer looses.\nYOU WIN!")
        elif sum_comp > sum_player:
            print("Computer wins.\nYOU LOSE!")
        elif sum_comp < sum_player:
            print("YOU WIN!")
        elif sum_comp == sum_player:
            print("It's a tie!")

    def show():
        print(f"Your cards are: {player_cards}")
        print("Your total is: " + str(sum_player))
        print(f"Computer's first card is: {computer_cards[0]}")
    def comp():
        print(f"Your cards are: {player_cards}")
        print("Your total is: " + str(sum_player))
        print(f"Computer's cards are: {computer_cards}")
        print(f"Computer's total is: {sum_comp}")

    to_draw = True
    while to_draw and sum_player <= 21:
        show()
        draw = input("Do you want to draw another card? Yes or No? ").lower()

        if draw == "no":
            comp()
            compare()
            to_draw = False
        elif draw == "yes":
            rand_int = cards[random.randint(0, 12)]
            player_cards.append(rand_int)
            sum_player += rand_int
            if sum_comp > 21 or sum_player > 21:
                comp()
            else:
                show()
            compare()
            to_draw = True

        play_again = input("Play Again? y or n ")
        if play_again == "n":
            print("Goodbye.")
            should_loop = False
            to_draw = False
