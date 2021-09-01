class GameState(object):
    """This class holds all relevent inforamtion and operations regarding the state of the game, and is mostly used by the AI player"""

    def __init__(self):
        self.turn = 'Z'
        self.AI_symbol = 'Z'
        self.player_symbol = 'Z'
        self.is_AI_mode = False
        self.previous = None
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

    def getValidMoves(self):
        """Returns a list of tuples for all the possible moves including the index in a one dimensional list."""
        result = []
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == '':
                    result.append((i,j,i*3+j))
        return result

    def clone(self):
        """Creates a perfect clone of the object then sets the parent as previous."""
        new_state = GameState()
        new_state.turn = self.turn
        new_state.AI_symbol = self.AI_symbol
        new_state.player_symbol = self.player_symbol
        new_state.is_AI_mode = self.is_AI_mode
        new_state.previous = self
        for i in range(0,3):
            for j in range(0,3):
                new_state.board[i][j] = self.board[i][j]
        return new_state

    def make_move(self, i, j):
        """Creates a new state and makes the moves with the given coordinates."""
        moves = self.getValidMoves()
        move = (i, j)
        for valid_move in moves:
            if move == valid_move[:-1]:
                new_state = self.clone()
                new_state.board[i][j] = new_state.turn
                new_state.turn = 'O' if new_state.turn == 'X' else 'X'
                return new_state
        print(f'The move {move} is not valid')
        return None


    def print_state(self):
        """Prints current state for debugging."""
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print(f'The current result is {self.check_winner()}')

    def clear_board(self):
        """Resets the board to have empty cells."""
        for i in range(0,3):
            for j in range(0,3):
                self.board[i][j] = ''

#    def set_cell(self, i, j, player):
#        self.board[i][j] == player


#p1 = GameState()
#p1.board[0][0] = 'X'
#p1.board[0][1] = 'X'
#p1.board[0][2] = 'X'
#p1.turn = 'O'
#p1.set_cell(1, 0, 'O')
#print(p1.getValidMoves())
#p1.clear_board()
#p1.board[1][0] = 'O'
#print(p1.getValidMoves())
#p1.board[2][1] = 'O'
#p1.print_state()
#p2 = p1.clone()
#p2.print_state()
#p1.board[0][2] = 'X'
#p1.print_state()
#p2.print_state()
#p2.previous.print_state()
#p3 = p1.make_move(1, 1)
#p1.print_state()
#p3.previous.print_state()
#p3.print_state()
#print(p1.turn)
#print(p3.turn)
