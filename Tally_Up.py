import tkinter as tk
import random

GRID_SIZE = 4
ITERATIONS_MAX = 64
ITERATIONS_MIN = 16
CELL_POSITION = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)] 

class GridGame():
    def __init__(self, window):
        self.window = window
        self.window.title("Tally_UP")

        self.grid = []
        for _ in range(GRID_SIZE):
            row = []
            for _ in range(GRID_SIZE):
                row.append(random.randint(1,3))
            self.grid.append(row)

        self.buttons = []
        for _ in range(GRID_SIZE):
                self.buttons.append([None] * GRID_SIZE) 

        self.selection = []
        
        self.message_label = tk.Label(window, text="", font=("Arial", 12))
        self.message_label.grid(row=GRID_SIZE + 1, column=0, columnspan=GRID_SIZE)

        self.generated_selections = []
        self.generated_directions = []

        self.build_grid()
        self.generate_path()

    def build_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                btn = tk.Button(self.window, text=str(self.grid[j][i]), font=("Arial", 20),
                                width=4, height=2, command=lambda x=j, y=i: self.cell_clicked(x, y))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[j][i] = btn

    def generate_path(self): 
        left = (-1,0)
        right = (1,0)
        up = (0,-1)
        down = (0,1)

        direction = [left,right,up,down]
        for _ in range(random.randint(ITERATIONS_MIN, ITERATIONS_MAX)):
            cell = random.choice(CELL_POSITION)
            x = cell[0]
            y = cell[1]
            illegal_neighbour = []

            if (x == 0 or y == 0):
                if (x == 0 and y == 0):
                    illegal_neighbour += [left, up]
                if (x == 0 and y != 0):
                    illegal_neighbour += [left]
                if (x != 0 and y == 0):
                    illegal_neighbour += [up]

            if (0 == 3 or y == 3):
                if (x == 3 and y == 3):
                    illegal_neighbour += [right, down]
                if (x == 3 and y != 3):
                    illegal_neighbour += [right]
                if (x != 3 and y == 3):
                    illegal_neighbour += [down]

            neighbours = [i for i in direction if i not in illegal_neighbour]
            self.generated_selections.append(cell)
            self.generated_directions.append(random.choice(neighbours))

    def cell_clicked(self, x, y):
        self.selection.append((x, y))
        self.buttons[x][y].config(bg="yellow")
        
        if len(self.selection) == 2:
            self.combine_cells()

    def combine_cells(self):
        (x1, y1), (x2, y2) = self.selection

        if (x1, y1) == (x2, y2):
            self.clear_selection()
            return

        if abs(x2 - x1) + abs(y2 - y1) != 1:
        #if abs(x2 - x1) | abs(y2 - y1) > 1: # logic to include diagonals 
            self.message_label.config(text="x Please select an adjacent cell", fg="red")
            self.clear_selection()
            return

        self.message_label.config(text="")

        self.grid[x2][y2] += self.grid[x1][y1]
        self.grid[x1][y1] = random.randint(1, 3)

        self.update_grid()
        self.clear_selection()

    def update_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.buttons[i][j].config(text=str(self.grid[i][j]), bg="lightgray")

    def clear_selection(self):
        for x, y in self.selection:
            self.buttons[x][y].config(bg="lightgray")
        self.selection.clear()

if __name__ == "__main__":
    window = tk.Tk()
    game = GridGame(window)
    window.mainloop()

