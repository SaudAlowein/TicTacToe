#!/usr/bin/env python3
import random
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
    global turn
    if turn == 'X':
        color = 'red'
    else:
        color = 'blue'
    buttons_list[index].config(state='disabled', text=turn, disabledforeground=color)
    winner = check_winner()
    if not winner == 'F':
        popup(winner)
    else:
        turn = 'O' if turn == 'X' else 'X'
        window.title(f'Tic Tac Toe ({turn}\'s turn)')

def check_winner():
    """Checks if there's winner and returns their symbol, 'D' if it's a draw, 'F' if the game is not finished."""
    if buttons_list[0]['state'] == 'disabled':
        if buttons_list[0]['text'] == buttons_list[1]['text'] == buttons_list[2]['text']:
            disable_buttons()
            return buttons_list[0]['text']
        elif buttons_list[0]['text'] == buttons_list[4]['text'] == buttons_list[8]['text']:
            disable_buttons()
            return buttons_list[0]['text']
        elif buttons_list[0]['text'] == buttons_list[3]['text'] == buttons_list[6]['text']:
            disable_buttons()
            return buttons_list[0]['text']
    if buttons_list[1]['state'] == 'disabled':
        if buttons_list[1]['text'] == buttons_list[4]['text'] == buttons_list[7]['text']:
            disable_buttons()
            return buttons_list[1]['text']
    if buttons_list[2]['state'] == 'disabled':
        if buttons_list[2]['text'] == buttons_list[4]['text'] == buttons_list[6]['text']:
            disable_buttons()
            return buttons_list[2]['text']
        elif buttons_list[2]['text'] == buttons_list[5]['text'] == buttons_list[8]['text']:
            disable_buttons()
            return buttons_list[2]['text']
    if buttons_list[5]['state'] == 'disabled':
        if buttons_list[5]['text'] == buttons_list[4]['text'] == buttons_list[3]['text']:
            disable_buttons()
            return buttons_list[5]['text']
    if buttons_list[8]['state'] == 'disabled':
        if buttons_list[8]['text'] == buttons_list[7]['text'] == buttons_list[6]['text']:
            disable_buttons()
            return buttons_list[8]['text']
    for button in buttons_list:
        if button['state'] == 'normal':
            break
        if button['state'] == 'disabled' and button == buttons_list[8]:
            disable_buttons()
            return 'D'
    return 'F'

def disable_buttons():
    """Disables all buttons on the board."""
    for button in buttons_list:
        button['state'] = 'disabled'

def initialize_board(frame):
    """Intializes the initial 3x3 board."""
    remove_frame()
    if len(buttons_list) > 0:
        buttons_list.clear()
    randomize_player()
    window.title(f'Tic Tac Toe ({turn}\'s turn)')
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
    remove_frame()
    window.configure(bg='Light Gray')
    frame = tk.Frame(master=window)
    welcome_font = font.Font(family='Halvetica', size=30)
    select_font = font.Font(size=15)
    welcome_label = tk.Label(master=frame, text='Welcome to Tic Tac Toe!', font=welcome_font)
    select_label = tk.Label(master=frame, text='Select the mode you would like to play.', font=select_font)
    start_2player_button = tk.Button(master=frame, text='2 Players', command=lambda frame=frame: initialize_board(frame))
    key_label = tk.Label(master=frame, text='You can press \'q\' to quit or \'m\' to return to this menu at any time.')
    welcome_label.pack(expand=True)
    select_label.pack(expand=True)
    start_2player_button.pack(expand=True)
    key_label.pack(expand=True)
    frame.pack(expand=True)
    set_frame(frame)

def randomize_player():
    """Randomizes first player symbol."""
    global turn
    turn = random.choice(('X','O'))

def end_to_menu(window):
    """Links popup button to the main menu."""
    window.destroy()
    initialize_menu()

def close_game(event):
    """Handle q key stroke to quit the game."""
    quit()

def main_menu(event):
    """Handle m key stroke to return to main menu."""
    initialize_menu()

if __name__ == '__main__':
    buttons_list = []
    current_frame = None
    window = tk.Tk()
    window.title('Tic Tac Toe')
    window.bind('q', close_game)
    window.bind('m', main_menu)
    initialize_menu()
    window.mainloop()
