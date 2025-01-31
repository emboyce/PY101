import random
VALID_PLAYS = ["rock", "paper", "scissors"]

def prompt(message):
    print(f"==> {message}")

def validate(user_input):
    if user_input in VALID_PLAYS:
        return True
    return False

def get_input(input_prompt):
    while True:
        prompt(input_prompt)
        input_variable = input()
        if validate(input_variable):
            return input_variable
        else:
            prompt("Invalid choice, please type choose again.")

def show_winner(winner):
    prompt(f"You chose {user_play_choice}.")
    prompt(f"Computer chose {computer_play_choice}.")
    if not winner == "tie":
        prompt(f"The winner is {winner}!")
    else:
        prompt(f"Tie, you chose the same!")

keep_playing = "y"

while not keep_playing == "n":
    
    user_play_choice = get_input(f"Choose one: {", ".join(VALID_PLAYS)}")

    computer_play_choice = random.choice(VALID_PLAYS)

    match user_play_choice, computer_play_choice:
        case "rock", "paper":
            show_winner("computer")
        case "rock", "scissors":
            show_winner("human")
        case "paper", "scissors":
            show_winner("computer")
        case "paper", "rock":
            show_winner("human")
        case "scissors", "rock":
            show_winner("computer")
        case "scissors", "paper":
            show_winner("human")
        case _:
            show_winner("tie")
    
    while True:
        prompt("Do you want to play again? y/n")
        keep_playing = input()
        if keep_playing.casefold() in ["y", "n"]:
            break
        prompt("Invalid choice, please type choose again.")

prompt("Goodbye!")
