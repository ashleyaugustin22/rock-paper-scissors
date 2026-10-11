import random
import os
import time

def clear_screen(): #COMPLETE
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear") 
def you_lose():
    print("""
    
YOU LOSE
    
GAME OVER

""")

    input("Press ENTER to go to MAIN MENU")
    
    clear_screen()
    return main_menu()
def you_win():
    print("""
YOU WIN!

""")
    input("Press ENTER to go to MAIN MENU")
    
    clear_screen()
    return main_menu()
def quit_game(): #COMPLETE
     while True:
        clear_screen()
        leave = input("Are you sure you want to leave the game? (Y/N)")
    
                    
        if leave.upper() == "Y":
            clear_screen()
            print("You are now leaving the game!...")
            time.sleep(5)
            clear_screen()
            return quit()
    
        elif leave.upper() == "N":
            time.sleep(1)
            clear_screen()
            return main_menu()
    
        else:
            print("Try Again")
            time.sleep(2)
            clear_screen()



class Player:

    def __init__(self, name):
        self.name = name

start = """

ROCK, PAPER, SCISSORS!


"""

game_choices = ["ROCK", "PAPER", "SCISSORS"]

def game_template_before(player, player_score, npc_score):
    game_template_before = f"""
{player.name}'s SCORE: {player_score}    OPPONENT's SCORE: {npc_score}


OPPONENT's Choice
----------------------------
....




{player.name}'s Choice
----------------------------
...






"""
    
    return game_template_before

def game_template_after(player, player_score, npc_score, player_choice, npc_choice):
    game_template_after = f"""
{player.name}'s SCORE: {player_score}    OPPONENT's SCORE: {npc_score}


OPPONENT's Choice
----------------------------
{npc_choice}




{player.name}'s Choice
----------------------------
{game_choices[int(player_choice) - 1]}






"""
    return game_template_after

def main_menu():
    main_menu_template = """
[1] NEW GAME
[2] INSTRUCTIONS
[3] QUIT
"""

    while True:
        print(start)
        print(main_menu_template)
        option = input("TYPE HERE: ")

        if option == "1":
            time.sleep(1)
            clear_screen()
            print("LOADING...")
            time.sleep(3)
            clear_screen()
            return gameplay(player)

        elif option == "2":
            time.sleep(1)
            clear_screen()
            instructions = """
Welcome to ROCK, PAPER, SCISSORS!

HOW TO PLAY:
============

You will be given three options against your opponent:

[1] ROCK
[2] PAPER
[3] SCISSORS

- Type in the NUMBER of the option you are choosing to reveal both
  you and your opponents choice.

- Whoever wins that round will earn 1 point until one person reaches 5 points.

- And whoever reaches 5 points wins the game!

Good luck and have fun!



"""
            while True:
                print(instructions)
                time.sleep(3)
                option = input("Ready to begin? Y/N (N will send you back to the main menu!)")

                if option.lower() == "y":
                    time.sleep(1)
                    clear_screen()
                    return gameplay(player)
                if option.lower() == "n":
                    time.sleep(1)
                    clear_screen()
                    return main_menu()

        elif option == "3":
            time.sleep(1)
            clear_screen()
            return quit_game()

        else:
            print("""
This is not an option. Please try again
""")
            time.sleep(2)
            clear_screen()            

def gameplay(player):
    player_score = 0
    npc_score = 0

    while player_score < 5 and npc_score < 5:
        print(game_template_before(player, player_score, npc_score))
        player_choice = input("""
[1] ROCK
[2] PAPER
[3] SCISSORS

Type number here: """)   
        
        if player_choice == "1":
            npc_choice = random.choice(game_choices)
            clear_screen()
            print(game_template_after(player, player_score, npc_score, player_choice, npc_choice))

            if npc_choice == "PAPER":
                npc_score += 1
            elif npc_choice == "SCISSORS":
                player_score += 1
            else:
                pass

            time.sleep(2)
            clear_screen()            



        elif player_choice == "2":
            npc_choice = random.choice(game_choices)
            clear_screen()            
            print(game_template_after(player, player_score, npc_score, player_choice, npc_choice))

            if npc_choice == "SCISSORS":
                npc_score += 1
            elif npc_choice == "ROCK":
                player_score += 1
            else:
                pass

            time.sleep(2)
            clear_screen()

        elif player_choice == "3":
            npc_choice = random.choice(game_choices)
            clear_screen()
            print(game_template_after(player, player_score, npc_score, player_choice, npc_choice))

            if npc_choice == "ROCK":
                npc_score += 1
            elif npc_choice == "PAPER":
                player_score += 1
            else:
                pass

            time.sleep(2)
            clear_screen()

        else:
            print("""
This is not an option. Please try again
""")
            time.sleep(2)
            clear_screen()

        if npc_score == 5:
            return you_lose()
            
        elif player_score == 5:
            return you_win()


clear_screen()
print(start)
time.sleep(2)

name = input("""
What is your name?

Type Here: """)

player = Player(name)


time.sleep(2)
clear_screen()
print(main_menu())