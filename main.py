from logic import *
from tkinter import *

window = Tk()

def start_state():
    main_grid[0] = sudoku_game()
    main_grid[0].create()
    main_grid[0].take_out()
    show_grid(main_grid[0].graph)
    button_archive['start_but'] = Button(window , text='solve !' , command=solve)
    button_archive['retry_but'] = Button(window , text='retry' , command=retry)
    button_archive['start_but'].grid(row= 9 , column= 0 , columnspan= 9)
    button_archive['retry_but'].grid(row=0 , column= 9 )

def retry():
    delete_grid()
    button_archive['start_but'].grid_forget()
    button_archive['retry_but'].grid_forget()
    start_state()

def solve():
    delete_grid()
    game = solution(main_grid[0].graph)
    i , j = 0 , 0
    if game.graph[i][j] != 0:
        o, i, j = game.nxt(i , j)
    
    game.solve_sudoku(i , j)
    show_grid(game.graph)
    button_archive['start_but'].grid_forget()


dic = {}

def show_grid(gr):
    for i in range(9):
        for j in range(9):
            dic[i, j] = Label(window , text=gr[i][j])

    for i in range(9):
        for j in range(9):
            dic[i, j].grid(row= i , column= j)

def delete_grid():
    for i in range(9):
        for j in range(9):
            dic[i, j].grid_forget()

button_archive = {}
main_grid = [0]
start_state()


window.mainloop()


