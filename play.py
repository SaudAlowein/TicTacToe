#!/usr/bin/env python3
import tkinter as tk
is_player_turn = True
def handle_move(event):
    if is_player_turn:
        print('X')
    else:
        print('O')
def initialize():
    """Intializes the initial 3x3 board"""
    buttons_list=[]
    window.title('Tic Tac Toe')
    for i in range(3):
        window.columnconfigure(i, weight=1)
        window.rowconfigure(i, weight=1)
        for j in range(3):
            frame = tk.Frame(master=window, relief=tk.FLAT, bg='black')
            frame.grid(row=i, column=j)
            cell = tk.Button(master=frame, text=f'({i},{j})', bg='white', activebackground='white',highlightbackground='black', width=80, height=15)
            buttons_list.append(cell)
            if i == 2 and j == 2:
                cell.grid(padx=(4,0), pady=(4,0), sticky='nsew')
            elif i == 0 and j == 0:
                cell.grid(padx=(0,4), pady=(0,4), sticky='nsew')
            elif i == 0 and j == 2:
                cell.grid(padx=(4,0), pady=(0,4), sticky='nsew')
            elif i == 2 and j == 0:
                cell.grid(padx=(0,4), pady=(4,0), sticky='nsew')
            elif i == 0:
                cell.grid(padx=4, pady=(0,4), sticky='nsew')
            elif j == 0:
                cell.grid(padx=(0,4), pady=4, sticky='nsew')
            elif i == 2:
                cell.grid(padx=4, pady=(4,0), sticky='nsew')
            elif j == 2:
                cell.grid(padx=(4,0), pady=4, sticky='nsew')
            else:
                cell.grid(padx=4, pady=4, sticky='nsew')
    return buttons_list

if __name__ == '__main__':
    window = tk.Tk()
    window.configure(bg='black')
    buttons_list = initialize()
    window.mainloop()
