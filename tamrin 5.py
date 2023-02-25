import random
from IPython.display import clear_output



class TextStyle:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



class TicTacToe:
    game_board = []
    playing = True
    player = ''
    player_round = ['pc', 'player']
    players = {'pc': 'X', 'player': 'O'}
    player_name = ''
    pc_piece_location = set()
    player_peice_location = set()
    win_locations = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {4, 5, 6}, {7, 8, 9}]

    def __init__(self):
        self.game_board = list(range(1, 10))
        self.player = random.choice(self.player_round)
        self.playerChoosePiece()
        self.startGame()

    def clearScreen(self):
        clear_output()
        print(f"{TextStyle.BLUE}Player round = {self.player} {TextStyle.RESET}", end='\t')
        print(f"{TextStyle.BLUE}Pieces info : player \'{self.player_name}\'={self.players['player']} , pc={self.players['pc']}{TextStyle.RESET}")
        print(f"{TextStyle.YELLOW}pc piece locations : {self.pc_piece_location} and player piece locations : {self.player_peice_location}{TextStyle.RESET}")
        print('-' * 80)
        # print(enumerate(self.game_board))
        for index, item in enumerate(self.game_board):
            if (index + 1) % 3 != 0:
                print(f"{item}", end='  |  ')
            else:
                print(f"{item}  ")
                print('-' * 15)

    def playerChoosePiece(self):
        self.player_name = input('Please input your name : ')
        player = ''
        while player not in ['x', 'X', 'o', 'O']:
            player = input("Please Choose Your Pieace: 'X' or 'O'")
        if player in ['X', 'x']:
            self.players['player'] = 'X'
            self.players['pc'] = 'O'
        else:
            self.players['player'] = 'O'
            self.players['pc'] = 'X'

    def playerChoosePlaceToPut(self):
        player_input = 0
        place_list = list(filter(self.filterListMethod, self.game_board))
        while player_input not in place_list:
            try:
                print(f"place numbers left : {place_list}")
                player_input = int(input("Please choose place number for your Piece : "))

            except:
                self.clearScreen()
        self.player_peice_location.add(player_input)
        self.game_board[player_input - 1] = self.players['player']

    def checkWin(self):
        for item in self.win_locations:
            if item.issubset(self.pc_piece_location):
                print(f"{TextStyle.GREEN}PC Wins : {item} {TextStyle.RESET}")
                return True
            elif item.issubset(self.player_peice_location):
                print(f"{TextStyle.GREEN}{self.player_name} Wins : {item} {TextStyle.RESET}")
                return True
        return False

    def pcChoosePlaceToPut(self):
        place_list = list(filter(self.filterListMethod, self.game_board))
        pc_input = random.choice(place_list)
        self.pc_piece_location.add(pc_input)
        self.game_board[pc_input - 1] = self.players['pc']

    def filterListMethod(self, number):
        if number in list(range(1, 10)):
            return True
        else:
            return False

    def checkBoard(self):
        place_list = list(filter(self.filterListMethod, self.game_board))
        if len(place_list) == 0:
            print(f"{TextStyle.GREEN}DRAW {TextStyle.RESET}")
            self.playing = False
            return True

    def startGame(self):
        while self.playing == True:
            if self.checkWin():
                break
            if self.checkBoard():
                break
            if self.player == 'player':
                self.clearScreen()
                self.playerChoosePlaceToPut()
                self.player = 'pc'
            else:
                self.pcChoosePlaceToPut()
                self.clearScreen()
                self.player = 'player'



game = TicTacToe()

