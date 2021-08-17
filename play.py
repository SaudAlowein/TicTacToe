#!/usr/bin/env python3
import tkinter as tk
import tkinter.font as font
from tkinter import Canvas
turn = 'X'
buttons_list = []
def handle_move(index):
    """Updates the board when an active cell is clicked."""
    global turn
    if turn == 'X':
        color = 'red'
    else:
        color = 'blue'
    buttons_list[index].config(state='disabled', text=turn, disabledforeground=color)
    winner = check_winner()
    if winner == 'D':
        print('It\'s a draw!')
    elif not winner == 'F':
        print(f'Player {turn} has won!')
    else:
        turn = 'O' if turn == 'X' else 'X'

def check_winner():
    """Checks if there's winner and returns their symbol, 'D' if it's a draw, 'F' if the game is not finished."""
    if buttons_list[0]['state'] == 'disabled':
        if buttons_list[0]['text'] == buttons_list[1]['text'] == buttons_list[2]['text']:
            return buttons_list[0]['text']
        elif buttons_list[0]['text'] == buttons_list[4]['text'] == buttons_list[8]['text']:
            return buttons_list[0]['text']
        elif buttons_list[0]['text'] == buttons_list[3]['text'] == buttons_list[6]['text']:
            return buttons_list[0]['text']
    if buttons_list[1]['state'] == 'disabled':
        if buttons_list[1]['text'] == buttons_list[4]['text'] == buttons_list[7]['text']:
            return buttons_list[1]['text']
    if buttons_list[2]['state'] == 'disabled':
        if buttons_list[2]['text'] == buttons_list[4]['text'] == buttons_list[6]['text']:
            return buttons_list[2]['text']
        elif buttons_list[2]['text'] == buttons_list[5]['text'] == buttons_list[8]['text']:
            return buttons_list[2]['text']
    if buttons_list[5]['state'] == 'disabled':
        if buttons_list[5]['text'] == buttons_list[4]['text'] == buttons_list[3]['text']:
            return buttons_list[5]['text']
    if buttons_list[8]['state'] == 'disabled':
        if buttons_list[8]['text'] == buttons_list[7]['text'] == buttons_list[6]['text']:
            return buttons_list[8]['text']
    for button in buttons_list:
        if button['state'] == 'normal':
            break
        if button['state'] == 'disabled' and button == buttons_list[8]:
            return 'D'
    return 'F'
def initialize():
    """Intializes the initial 3x3 board"""
    buttons_list=[]
    window.title('Tic Tac Toe')
    move_font = font.Font(family='Halvetica', weight='bold', size=30)
    for i in range(3):
        for j in range(3):
            #window.columnconfigure(i, weight=1)
            #window.rowconfigure(j, weight=1)
            frame = tk.Frame(master=window, relief=tk.FLAT, bg='black')
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
    return buttons_list

if __name__ == '__main__':
    window = tk.Tk()
    window.configure(bg='black')
    window.geometry('950x950')
    window.grid_columnconfigure((0,1,2), weight=1)
    window.grid_rowconfigure((0,1,2), weight=2)
    window.grid_rowconfigure(0, weight=1)
    buttons_list = initialize()
    window.mainloop()
