import random

computer_number = random.randint(1, 100)

player_input = input("Guess the number (1-100): ")

while player_input != computer_number:

    if not player_input.isdigit():
        print("Invalid input -> please select a number...")
        continue

    if int(player_input) < computer_number:
        ask_higher = ["Try a higher one: ", "Wrong one ... maybe higher is where you should look: ",
                      "Don't give up ... search higher: ", "Check you crystal ball for a higher guess: "]
        player_input = input("".join(random.sample(ask_higher, k=1)))
    elif int(player_input) > computer_number:
        ask_lower = ["You are too high ... look out for the sun: ", "Dig it lower: ",
                     "It's too high ... I get dizzy: ", "Keep it low: "]
        player_input = input("".join(random.sample(ask_lower, k=1)))
    else:
        congrats = ["Hooray ... that's the one!", "You are amazing ... this is the number!",
                    "What a Champion ... you are ready for the Olympics!", "Congratulations ... Correct guess!"]
        print("".join(random.sample(congrats, k=1)))
        break

exit()
