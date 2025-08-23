import tkinter as tk
import random
import copy

GRID_SIZE = 4
ITERATIONS_MAX = 64
ITERATIONS_MIN = 16
CELL_POSITION = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)] 
SET = [1,2,3,'-','*','x2']
WEIGHT = [0.25,0.30,0.30,0.05,0.05,0.05]

class GridGame():
    def __init__(self, window):
        self.window = window
        self.window.title("Tally_UP")

        self.new_game_btn = tk.Button(self.window, text="new game", width=8, height=2, command=lambda : self.reset_game())
        self.new_game_btn.grid(row=0, column=0, columnspan=GRID_SIZE)
        self.build_game()

    def build_game(self):
        self.grid = []
        for _ in range(GRID_SIZE):
            row = []
            for _ in range(GRID_SIZE):
                row.append(random.choices(SET,WEIGHT)[0])
            self.grid.append(row)

        self.buttons = []
        for _ in range(GRID_SIZE):
                self.buttons.append([None] * GRID_SIZE) 

        self.selection = []
        self.message_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.message_label.grid(row=GRID_SIZE + 101, column=0, columnspan=GRID_SIZE)

        self.generated_selections = []
        self.generated_directions = []
        self.next_value = []
        self.target = []

        self.target_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.target_label.grid(row=2, column=0, columnspan=GRID_SIZE)

        self.build_grid()
        self.generate_path()
        self.generate_target()

    def build_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                btn = tk.Button(self.window, text=str(self.grid[j][i]), font=("Arial", 20),
                                width=4, height=2, command=lambda x=j, y=i: self.cell_clicked(x, y))
                btn.grid(row=i+100, column=j, padx=2, pady=2)
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

            if (x == 3 or y == 3):
                if (x == 3 and y == 3):
                    illegal_neighbour += [right, down]
                if (x == 3 and y != 3):
                    illegal_neighbour += [right]
                if (x != 3 and y == 3):
                    illegal_neighbour += [down]

            neighbours = [i for i in direction if i not in illegal_neighbour]
            self.generated_selections.append(cell)
            self.generated_directions.append(random.choice(neighbours))        
            self.next_value.append(random.choices(SET,WEIGHT)[0]) 

    def generate_target(self):
        cp_grid = copy.deepcopy(self.grid)
        cp_selection = copy.deepcopy(self.generated_selections)
        cp_direction = copy.deepcopy(self.generated_directions)
        cp_value = copy.deepcopy(self.next_value)

        target = 1

        for _ in range(len(cp_selection)):
            selected = cp_selection.pop(0)
            direction = cp_direction.pop(0)
            value = cp_value.pop(0)

            (x1, y1) = selected
            (dir_x, dir_y) = direction

            (x2, y2) = (x1 + dir_x, y1 + dir_y)

            result = self.operator_logic((cp_grid[x1][y1]),(cp_grid[x2][y2]), False)
            if result == "illegal operation":
                pass
            else:
                cp_grid[x2][y2] = result
                cp_grid[x1][y1] = value
                
                if (type(result) == int) and (result > target):
                    target = result

        self.target = target
        self.target_label.config(text=f"your target is {self.target}", fg="black")

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
            self.message_label.config(text="x Please select an adjacent cell", fg="red")
            self.clear_selection()
            return

        self.message_label.config(text="")

        result = self.operator_logic((self.grid[x1][y1]),(self.grid[x2][y2]), True)
        if result == "illegal operation":
            pass
        else:
            self.grid[x2][y2] = result

            self.grid[x1][y1] = self.next_value.pop(0) if len(self.next_value) > 0  else random.choices(SET,WEIGHT)[0]

            if (self.grid[x2][y2] == self.target):
                self.target_label.config(text="You win!!", fg="green")
                return
            self.update_grid()
        self.clear_selection()

    def operator_logic(self, cell_1, cell_2, user_move):
        if type(cell_1) == str and type(cell_2) == str:

            if cell_1 == '*' and cell_2 == '*':
                return('^2')
            elif cell_1.startswith('x') and cell_2.startswith('x'):
                a = int(cell_1[1:])
                b = int(cell_2[1:])

                if (a*b) > 0 and (a*b) < 16:
                    result = 'x' + str(a*b)
                    return(result)
                else:
                    if user_move == True:
                        self.message_label.config(text="multipler out of range: 0 to 16", fg="red") 
                    return("illegal operation")
            else:
                if user_move == True:
                    self.message_label.config(text="Illegal Operation", fg="red")
                return("illegal operation")
                

        elif type(cell_1) == int and type(cell_2) == str:

            if cell_2.startswith('x'):
                a = int(cell_2[1:])
                result = a*cell_1
                return(result)
            if cell_2 == '*':
                if (cell_1 < 0 or cell_1 > 16) and user_move == True:
                    self.message_label.config(text="multipler out of range: 0 to 16", fg="red")
                    return("illegal operation")

                result = 'x' + str(cell_1)
                return(result)
            if cell_2 == '^2':
                result = cell_1*cell_1
                return(result)
            if cell_2 == '-':
                result = -cell_1
                return(result)

        elif type(cell_1) == str and type(cell_2) == int:

            if cell_1.startswith('x'):
                a = int(cell_1[1:])
                result = a*cell_2
                return(result)
            if cell_1 == '*':
                if (cell_2 < 0 or cell_2 > 16) and user_move == True:
                    self.message_label.config(text="multipler out of range: 0 to 16", fg="red")
                    return("illegal operation")
                result = 'x' + str(cell_2)
                return(result)
            if cell_1 == '^2':
                result = cell_2*cell_2
                return(result)
            if cell_1 == '-':
                result = -cell_2
                return(result)

        else:
            result = cell_1+cell_2
            return(result)

    def update_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.buttons[i][j].config(text=str(self.grid[i][j]), bg="lightgray")

    def clear_selection(self):
        for x, y in self.selection:
            self.buttons[x][y].config(bg="lightgray")
        self.selection.clear()

    def reset_game(self):
        self.target_label.config(text="")
        self.build_game()

if __name__ == "__main__":
    window = tk.Tk()
    game = GridGame(window)
    window.mainloop()

