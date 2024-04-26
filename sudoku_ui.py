import tkinter as tk
import numpy as np
from sudoku_solver import solving_algorithm
from tkinter import messagebox

class SudokuInputApp:
  def __init__(self, master):
    self.master = master
    master.title("Sudoku Input")

    self.entries = [[None]*9 for _ in range(9)]

    vcmd = master.register(self.validate_input)

    for i in range(9):
      for j in range(9):
        self.entries[i][j] = tk.Entry(master, width=2, font=('Arial', 30), validate='key', validatecommand=(vcmd, '%P'))
        self.entries[i][j].grid(row=i, column=j)

        self.entries[i][j].bind('<Left>', lambda event, row=i, col=j: self.move_focus(event, row, col-1))
        self.entries[i][j].bind('<Right>', lambda event, row=i, col=j: self.move_focus(event, row, col+1))
        self.entries[i][j].bind('<Up>', lambda event, row=i, col=j: self.move_focus(event, row-1, col))
        self.entries[i][j].bind('<Down>', lambda event, row=i, col=j: self.move_focus(event, row+1, col))

    self.solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
    self.solve_button.grid(row=9, columnspan=9)

    '''testArray = np.array([[6,3,0,0,2,0,0,0,9],
                        [0,4,0,5,3,1,0,0,2],
                        [0,7,5,0,4,9,0,3,1],
                        [8,0,0,4,0,6,1,0,0],
                        [0,0,0,2,1,0,3,9,6],
                        [0,0,0,7,0,3,2,0,4],
                        [3,8,7,0,0,0,4,0,0],
                        [4,0,2,1,0,0,0,6,3],
                        [0,0,0,0,7,0,0,0,0]])
    
    for i in range(9):
      for j in range(9):
        testValue = testArray[i][j]
        if testValue == 0:
          pass
        else:
          self.entries[i][j].insert(0, str(testValue))'''

  def move_focus(self, event, row, col):
    row = max(0, min(row, 8))
    col = max(0, min(col, 8))
    self.entries[row][col].focus_set()
  
  def validate_input(self, new_text):
    if new_text == '' or (new_text.isdigit() and 1 <= int(new_text) <=9):
      return True
    return False

  def solve_sudoku(self):
    array = np.zeros((9, 9), dtype=int)
    for i in range(9):
      for j in range(9):
        if self.entries[i][j].get() == '':
          pass
        else:
          array[i][j] = int(self.entries[i][j].get())
    solvedArray = solving_algorithm(array)
    if solvedArray == False:
      messagebox.showinfo("Unsolvable Sudoku", "This Sudoku puzzle is unsolvable")
      return
    for i in range(9):
      for j in range(9):
        if len(self.entries[i][j].get()) != 0:
          pass
        else:
          solvedValue = solvedArray[i][j]
          self.entries[i][j].insert(0, str(solvedValue))
          self.entries[i][j].config(bg="light green")

def main():
  root = tk.Tk()
  app = SudokuInputApp(root)
  root.mainloop()

if __name__ == "__main__":
  main()