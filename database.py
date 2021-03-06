import random
from PIL import Image, ImageTk

IMAGE_PATH = r"./images/"

#the pile
LETTERS = {"a": 13, "b": 3, "c": 3, "d": 6, "e": 18, "f": 3, "g": 4,
           "h": 3, "i": 12, "j": 2, "k": 2, "l": 5, "m": 3, "n": 8,
           "o": 11, "p": 3, "q": 2, "r": 9, "s": 6, "t": 9, "u": 6,
           "v": 3, "w": 3, "x": 2, "y": 3, "z": 2}


# the class for creating images
class CreateCanvasObject(object):
    def __init__(self, canvas, letter, xpos, ypos):
        self.canvas = canvas
        self.xpos, self.ypos = xpos, ypos

        self.tk_image = ImageTk.PhotoImage(
            Image.open(IMAGE_PATH + letter + ".jpg").resize((32,32)))

        self.image_obj = canvas.create_image(
            xpos, ypos, image=self.tk_image)

        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.move_flag = False

    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y

            self.canvas.move(self.image_obj,
                             new_xpos - self.mouse_xpos, new_ypos - self.mouse_ypos)

            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y

    def release(self, event):
        self.move_flag = False


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
        # draw 3
        n = 3
        while n > 0:
            n -= 1
            self.draw(letters)

        chosen_letter = choose_letter(self.tiles)

        self.tiles[chosen_letter] -= 1
        letters[chosen_letter] += 1


def choose_letter(letters): #letters that you have in hand
    #insert routine here to choose a letter
    print(letters)
    letter = str(input("select a letter to dump"))
    for let, value in letters.items():
        if let == letter and value > 0:
            return letter
    else:
        print("error, you have no such letter! try again!")
        pass


if __name__ == '__main__':
    # draw a board
    new_game = Game("new_game")
    Lyndon = Player("Lyndon")
    new_game.add_player(Lyndon)
    new_game.distribute()
    Lyndon.dump(new_game.letters)