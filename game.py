import random



game_choice = ["ROCK", "PAPER", "SCISSORS"]
game_template_before = """
WINS: {player_score}                 WINS: {npc_score}
    {player.name}                          OPPONENT
---------------------                --------------------
         ...                                  ...





"""
game_template_after = """

    {player.name}                          OPPONENT
---------------------                --------------------
      {option}                           {npc_choice}





"""


class Player:
    choices = []
    

    def __init__(self, name):
        self.name = name



    def save_choice(self, choice):
        self.choices.append(choice)


    


def easy_npc():


    



def med_npc():
    pass


def hard_npc():
    pass