class GameState(object):
    """This class holds all relevent inforamtion and operations regarding the state of the game, and is mostly used by the AI player"""

    def __init__(self):
        self.turn = 'Z'
        self.AI_symbol = 'Z'
        self.board = []
        row = []
        for i in range(0,3):
            for j in range(0,3):
                row.append('')
            self.board.append(row)
            row = []

    def check_winner(self):
        """Checks if there's winner and returns their symbol, 'D' if it's a draw, 'F' if the game is not finished."""
        if not self.board[0][0] == '' and self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return self.board[0][0]
        if not self.board[1][0] == '' and self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return self.board[1][0]
        if not self.board[2][0] == '' and self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return self.board[2][0]
        if not self.board[0][0] == '' and self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return self.board[0][0]
        if not self.board[0][1] == '' and self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return self.board[0][1]
        if not self.board[0][2] == '' and self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return self.board[0][2]
        if not self.board[0][0] == '' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if not self.board[0][2] == '' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        for row in self.board:
            for cell in row:
                if cell == '':
                    return 'F'
        return 'D'

    def print_state(self):
        """Prints current state for debugging"""
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print(f'The current result is {self.check_winner()}')

    def clear_board(self):
        for i in range(0,3):
            for j in range(0,3):
                self.board[i][j] = ''

#    def set_cell(self, i, j, player):
#        self.board[i][j] == player


#p1 = GameState()
#p1.board[0][0] = 'X'
#p1.board[0][1] = 'X'
#p1.board[0][2] = 'X'
#p1.set_cell(1, 0, 'O')
#p1.clear_board()
#p1.board[1][0] = 'O'
#p1.board[2][1] = 'O'
#p1.print_state()
