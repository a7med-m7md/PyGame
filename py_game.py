import time
import random

# Declare a global score variable to track the player's score.
TOTAL_SCORE = 0

# print message and you can customize the delay 
def print_pause(msg, delay=2):
    print(msg)
    time.sleep(delay)


# Display Some information that can user choose his path depending on
def field(weapons, random_enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        entered_num = input("(Please enter 1 or 2.)")
        if entered_num == "1":
            house(weapons, random_enemy)
            break
        elif entered_num == "2":
            cave(weapons, random_enemy)
            break


# game into messages and call to the starter
def game_starter(weapons, random_enemy):
    print_pause(
        "You find yourself standing in an open field, "
        + "filled with grass and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a "
        + random_enemy
        + " is somewhere around here, "
        + "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective) "
        + "rusty old magic wand."
    )
    field(weapons, random_enemy)


# restart game choices
def restart_game():
    game_threshold = -5
    if (game_threshold < TOTAL_SCORE):
        replay = input("Would you like to play again? (y/n)").lower()
        if replay == "n":
            print_pause("Your Score: " + TOTAL_SCORE)
            print_pause("Thanks for playing! See you next time.")
        elif replay == "y":
            print_pause("Excellent! Restarting the game ...")
            play_game()
        else:
            restart_game()
    else:
        print_pause("Game Over!, see you soon")


# If user choose to go to house do some thing
# depending on he has something in weapons list or not
def house(weapons, random_enemy):
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps a "
        + random_enemy
        + "."
    )
    print_pause("Eep! This is the " + random_enemy + "'s house!")
    print_pause("The " + random_enemy + " finds you!")
    if "wand" in weapons:
        print_pause(
            "You feel a bit under-prepared for this, what with only "
            + "having a tiny, rusty old magic wand."
        )
    do_action_depending_on_weapon(weapons, random_enemy)


# If user choose to go to cave it will do
# something depending on he has wand in weapons object or not
def cave(weapons, random_enemy):
    if "wand" in weapons:
        print_pause("You peer cautiously into the cave.")
        print_pause(
            "You've been here before, and gotten all the good "
            + "stuff. It's just an empty cave now."
        )
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Wand of Ogoroth!")
        print_pause(
            "You discard your rusty old magic wand "
            + "and take the Wand of Ogoroth with you."
        )
        print_pause("You walk back out to the field.")
        weapons.append("wand")
    field(weapons, random_enemy)


# If it has a wand as a weapon the player wins
def has_wand(random_enemy):
    global TOTAL_SCORE
    print_pause(
        "As the " + random_enemy + " moves to cast a spell, "
        "you unsheath your new sword."
    )
    print_pause(
        "The Want of Ogoroth shines brightly in your hand "
        + "as you brace yourself for the attack."
    )
    print_pause(
        "But the "
        + random_enemy
        + "takes one look at your shiny new wand and runs away!"
    )
    print_pause(
        "You have rid the town of the " + random_enemy + ". You are victorious!"
    )
    TOTAL_SCORE += 1
    print_pause("You win, current score: " + str(TOTAL_SCORE))


def do_action_depending_on_weapon(weapons, random_enemy):
    global TOTAL_SCORE
    while True:
        user_choice = input(
            "Would you like to (1) cast a spell or (2) run away?")
        if user_choice == "1":
            if "wand" in weapons:
                has_wand(random_enemy)
            else:
                print_pause("You do your best...")
                print_pause(
                    "but your rusty olg magic wand is no match for the "
                    + random_enemy
                    + "."
                )
                print_pause("You have been turned into a frog!")
                TOTAL_SCORE -= 1
                print_pause("You lose, current score: " + str(TOTAL_SCORE))
            restart_game()
            break
        if user_choice == "2":
            print_pause(
                "You run back into the field. Luckily, "
                + "you don't seem to have been followed."
            )
            field(weapons, random_enemy)
            break


def play_game():
    weapons = []
    enemy = ["pirate", "troll", "dragon", "gorgon", "wicked fairie"]
    random_enemy = random.choice(enemy)
    game_starter(weapons, random_enemy)


play_game()
