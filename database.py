import random

letters = {"a": 3, "b": 3, "c": 3, "d": 3, "e": 3, "f": 3, "g": 3,
           "h": 3, "i": 3, "j": 3, "k": 3, "l": 3, "m": 3, "n": 3,
           "o": 3, "p": 3, "q": 3, "r": 3, "s": 3, "t": 3, "u": 3,
           "v": 3, "w": 3, "x": 3, "y": 3, "z": 3
           }

no_of_players = sum(players)

class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = {}

    def draw(self):
        if sum(letters.values()) > no_of_players:
            letter = random.choice(list(letters.keys()))
            if letters[letter] > 0:
                letters[letter] -= 1
                self.tiles[letter] += 1

def peel():
    #every player gets one more letter at random


def dump():
    #return 1
    #pick up 3

#check if no of tiles remaining is < no. of players.

