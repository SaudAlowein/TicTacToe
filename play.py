#!/usr/bin/env python3
from gamestate import GameState
import random
import math
import tkinter as tk
import tkinter.font as font
from tkinter import Canvas

def popup(winner):
    """Display end screen in a new window."""
    new_window= tk.Tk()
    new_window.title('End screen')
    new_window.geometry('300x200')
    new_window.bind('q', close_game)
    new_window.bind('m',lambda event: handle_q_popup(event, new_window))
    label_font = font.Font(family='Halvetica', size=25)
    if winner == 'D':
        label = tk.Label(master=new_window, text='The game is a draw!', font=label_font)
    else:
        label = tk.Label(master=new_window, text=f'The winner is {winner}', font=label_font)
    button = tk.Button(master=new_window, text='main menu', command=lambda window=new_window: end_to_menu(window))
    label.pack(expand=True)
    button.pack(expand=True)
    new_window.mainloop()

def handle_q_popup(event, new_window):
    """Handle m key stroke from end screen."""
    new_window.destroy()
    initialize_menu()

def handle_move(index):
    """Updates the board when an active cell is clicked."""
#    global current_state.turn
    if current_state.turn == 'X':
        color = 'red'
#        current_state.set_cell(int(index/3), int(index%3), 'X')
        current_state.board[int(index/3)] [int(index%3)] = 'X'
    else:
        color = 'blue'
#        current_state.set_cell(int(index/3), int(index%3), 'O')
        current_state.board[int(index/3)] [int(index%3)] = 'O'
    current_state.previous_move = (int(index/3), int(index%3))
    buttons_list[index].config(state='disabled', text=current_state.turn, disabledforeground=color)
    winner = current_state.is_terminal()
    #current_state.print_state()
#    print(winner)
    if not winner == 'F':
        disable_buttons()
        popup(winner)
    else:
        current_state.turn = 'O' if current_state.turn == 'X' else 'X'
        window.title(f'Tic Tac Toe ({current_state.turn}\'s current_state.turn)')
        if current_state.is_AI_mode and current_state.turn == current_state.AI_symbol:
            findMove()

def disable_buttons():
    """Disables all buttons on the board."""
    for button in buttons_list:
        button['state'] = 'disabled'

def initialize_board(frame):
    """Intializes the initial 3x3 board."""
    current_state.clear_board()
    remove_frame()
    if len(buttons_list) > 0:
        buttons_list.clear()
    randomize_player()
    window.title(f'Tic Tac Toe ({current_state.turn}\'s turn)')
    window.configure(bg='black')
    window.geometry('950x950')
    move_font = font.Font(family='Halvetica', weight='bold', size=30)
    frame = tk.Frame(master=window, relief=tk.FLAT, bg='black')
    for i in range(3):
        for j in range(3):
            frame.grid(row=i, column=j)
            cell = tk.Button(master=frame, text='', font=move_font, bg='white', activebackground='white',highlightbackground='black', width=10, height=5, command=lambda index=i*3+j: handle_move(index))
            buttons_list.append(cell)
            if i == 2 and j == 2:
                cell.grid(row=i, column=j, padx=(4,0), pady=(4,0), sticky='nsew')
            elif i == 0 and j == 0:
                cell.grid(row=i, column=j, padx=(0,4), pady=(0,4), sticky='nsew')
            elif i == 0 and j == 2:
                cell.grid(row=i, column=j, padx=(4,0), pady=(0,4), sticky='nsew')
            elif i == 2 and j == 0:
                cell.grid(row=i, column=j, padx=(0,4), pady=(4,0), sticky='nsew')
            elif i == 0:
                cell.grid(row=i, column=j, padx=4, pady=(0,4), sticky='nsew')
            elif j == 0:
                cell.grid(row=i, column=j, padx=(0,4), pady=4, sticky='nsew')
            elif i == 2:
                cell.grid(row=i, column=j, padx=4, pady=(4,0), sticky='nsew')
            elif j == 2:
                cell.grid(row=i, column=j, padx=(4,0), pady=4, sticky='nsew')
            else:
                cell.grid(row=i, column=j, padx=4, pady=4, sticky='nsew')
    set_frame(frame)

def remove_frame():
    """Helper function that destroyes current frame."""
    if not current_frame == None:
        current_frame.destroy()
    set_frame(None)

def set_frame(frame):
    """Setter function to update the gobal variable current_frame."""
    global current_frame
    current_frame = frame

def initialize_menu():
    """Create the main menu frame."""
    current_state.is_AI_mode = False
    remove_frame()
    window.configure(bg='Light Gray')
    frame = tk.Frame(master=window)
    welcome_font = font.Font(family='Halvetica', size=30)
    select_font = font.Font(size=15)
    welcome_label = tk.Label(master=frame, text='Welcome to Tic Tac Toe!', font=welcome_font)
    select_label = tk.Label(master=frame, text='Select the mode you would like to play.', font=select_font)
    start_2player_button = tk.Button(master=frame, text='2 Players', command=lambda frame=frame: initialize_board(frame))
    start_AI_button = tk.Button(master=frame, text='Play against an AI', command=lambda frame=frame: AI_mode(frame))
    key_label = tk.Label(master=frame, text='You can press \'q\' to quit or \'m\' to restate.turn to this menu at any time.')
    welcome_label.pack(expand=True)
    select_label.pack(expand=True)
    start_2player_button.pack(expand=True)
    start_AI_button.pack(expand=True)
    key_label.pack(expand=True)
    frame.pack(expand=True)
    set_frame(frame)

def AI_mode(frame):
    """Starts AI mode"""
    current_state.is_AI_mode = True
    initialize_board(frame)
    if current_state.turn == current_state.AI_symbol:
        findMove()

def findMove():
    """Called by maximizing player to find and make the best move with a max depth of 4."""
    global value
    depth = 4
    final_move = (-1, -1)
    moves = current_state.getValidMoves()
    value = 0
    for valid_move in moves:
        move = valid_move[:-1]
        temp=minimax(current_state.make_move(move[0], move[1]), depth - 1)
#        print(f'value:{value} <= temp:{temp}')
        if value <= temp:
            final_move = move
            value = temp
    if final_move == (-1, -1):
        print('No move picked, making first viable move.')
        final_move = moves[0][:-1]
    index=final_move[0]*3+final_move[1]
    print(f'index:{index}, value:{value}')
    print('========================================================================')
    handle_move(index)


def minimax(state, depth):
    """Creates the game tree and traverses it"""
    if not (state.is_terminal() == 'F') or depth == 0:
        print(f'Entering terminal state with depth: {depth}')
        state.print_state()
        value = utility(state, depth)
        return value
    moves = state.getValidMoves()
#    print(f'In minimax, moves:{moves}, value:{value}, depth:{depth}')
    state.print_state()
    move = (-1, -1)
    if state.turn == state.AI_symbol:
        value = -math.inf
        for valid_move in moves:
#            move = valid_move[:-1]
            print(f'checking move:{valid_move}')
            value = max(value, minimax(state.make_move(valid_move[0], valid_move[1]), depth - 1))
        return value
    else:
        value = math.inf
        for valid_move in moves:
#            move = valid_move[:-1]
            print(f'checking move:{valid_move}')
            value = min(value, minimax(state.make_move(valid_move[0], valid_move[1]), depth - 1))
        return value

def utility(state, depth):

    if state.is_terminal() == state.AI_symbol:
        score = 9999
        if depth == 3:
            score = 10000
    elif state.is_terminal() == state.player_symbol:
        score = -9999
        if depth == 3:
            score = -10000
    elif state.is_terminal() == 'D':
        score = 0
    else:
        score = random.choice((0,1,2,3,4,5,6,7,8,9))
    i = state.previous_move[0]
    j = state.previous_move[1]
    print(f'Score:{score}')
    return score

def check_adjecent(state):
    i = state.previous_move[0]
    j = state.previous_move[1]
    previous_symbol = state.board[i][j]
    score = 0
    #if i == 1 and j == 1:


#def check_one_off_win(state):
#    """AI player uses this function to check for moves that need immediate action. Returns a tuple of the cell and the player that needs to play there to win."""
#    count_player_symbol = 0
#    count_AI_symbol = 0
#    temp_symbol = ''
#    temp = (-1, -1)
#    while i in range(0,3):
        #if not state.board[i][0] == '' and (state.board[i][1] == state.board[i][0] or state.board[i][2] == state.board[i][0]):
        #    temp_symbol = state.board[]
#        while j in range(0,3):


def randomize_player():
    """Randomizes first player symbol and AI player."""
#    global current_state.turn
    current_state.turn = random.choice(('X','O'))
    current_state.AI_symbol = random.choice(('X','O'))
    current_state.player_symbol = 'O' if current_state.AI_symbol == 'X' else 'X'

def end_to_menu(window):
    """Links popup button to the main menu."""
    window.destroy()
    initialize_menu()

def close_game(event):
    """Handle q key stroke to quit the game."""
    quit()

def main_menu(event):
    """Handle m key stroke to restate.turn to main menu."""
    initialize_menu()

if __name__ == '__main__':
    current_state = GameState()
    #current_state.board[0][0] = 'O'
    #current_state.print_state()
    value = math.inf
    buttons_list = []
    current_frame = None
    window = tk.Tk()
    window.title('Tic Tac Toe')
    window.bind('q', close_game)
    window.bind('m', main_menu)
    initialize_menu()
    window.mainloop()
