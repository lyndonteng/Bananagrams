import random

#the pile
LETTERS = {"a": 13, "b": 3, "c": 3, "d": 6, "e": 18, "f": 3, "g": 4,
           "h": 3, "i": 12, "j": 2, "k": 2, "l": 5, "m": 3, "n": 8,
           "o": 11, "p": 3, "q": 2, "r": 9, "s": 6, "t": 9, "u": 6,
           "v": 3, "w": 3, "x": 2, "y": 3, "z": 2}

#the game
class Game:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.letters = LETTERS

    def add_player(self, player):
        self.players.append(player)

    def distribute(self):
        if len(self.players) <= 4:
            n = 21
        elif len(self.players) <= 6:
            n = 15
        else:
            n = 11

        while n > 0:
            n -= 1
            for player in self.players:
                player.draw(self.letters)

    def peel(self):
        # all players draw one card
        if sum(self.letters.values()) > len(self.players):
            for player in self.players:
                player.draw(self.letters)


# the player
class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = {}

    def draw(self, letters):
        letter = random.choice(list(letters.keys()))
        if letters[letter] > 0:
            letters[letter] -= 1
            if letter not in self.tiles.keys():
                self.tiles[letter] = 1
            else:
                self.tiles[letter] += 1

    def dump(self, letters):
        # return 1
        #draw 3
        n = 3
        while n > 0:
            self.draw(letters)
        pass


if __name__ == '__main__':
    new_game = Game("new_game")
    Lyndon = Player("Lyndon")
    new_game.add_player(Lyndon)
    new_game.distribute()