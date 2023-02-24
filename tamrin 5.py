import os
import random
from IPython.display import clear_output


class TicTacToe:
    game_board = []
    playing = True
    player = 0
    player_piece = {1: 'X', 2: 'O'}
    player_character = {1: 'PC', 2: 'You'}
    player_input = ''

    def __init__(self):
        self.game_board = list(range(1, 10))
        self.playerChoosePiece()
        pass

    def clearScreen(self):
        clear_output()
        print(f"Player = {self.player} ")
        print('-' * 80)

        for item in self.game_board:
            if item % 3 != 0:
                print(f"{item}", end='  |  ')
            else:
                print(f"{item}  ")
                print('-' * 15)

    def playerChoosePiece(self):

        while self.player_input not in ['x', 'X', 'o', 'O']:
            self.player_input = input("Please Choose Your Pieace: 'X' or 'O'")

    def playerChoosePlaceToPut(self):
        self.player_input = 0
        place_list = filter(self.filterListMethod, self.game_board)
        while self.player_input not in place_list:
            try:
                print(place_list, end=' , ')
                self.player_input = int(input("Please Choose Number for your Piece : "))
            except:
                self.clearScreen()



    def filterListMethod(self,number):
        if number in list(range(1,10)):
            return True
        else:
            return False

    def startGame(self):
        while self.playing == True:
            self.clearScreen()
            self.inputPlayer()
            pass

    def inputPlayer(self):
        try:
            pass
        except:
            pass


game = TicTacToe()
game.clearScreen()
