import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor: )" )
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

response = get_choices()
print(response)
choices = get_choices()
print(choices)
