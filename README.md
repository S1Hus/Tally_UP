# Tally_UP
Grid based math Game that you combine numbers together to reach a target sum.


# How to play the Game.
Players can select a cell and combine it with their orthogonal/cardinal neighnbours.

When combining two cells, the one selected first will be replaced with a new value. See the 'How the game works internally' for  more details.


### Rules of the game

All the legal moves can be categories into one of the following moves:

- Number and Number: when two numbers are selected their values are added together. The result is placed in the cell of the second number that was selected.
**Note: The cell of the first number will then be replaced with the value of the next piece. This is a similar feature to how many popular variants of tetris show the next piece to be played**

- Number and Operator: The operator will be prefixed before the number. For example if the number 4 and operator 'x' are combined the result will be a 'x4' cell which will then be able to quadruple the value of the next cell it is combined with.
**Players can further combine these cells to make creater values i.e. x4 combined with x2 to make x8**
**Note- For this version of Tally_UP their is a max value of x16**

- Operator and Operator: As there are only two operators that are available in the game it is easiest two explain both separately.
+ Combining 'x' cells- the result is a squared operator which can then be combined with a number to square its value i.e. ^2 combined with 3 results in the value of 9.

# How the game works internally

Randomly generate a 4x4 cell with values contained in the set [0,1,2,3,-,*].

Randomly generate a list of next pieces by randomly selecting a value from the default set (see above line).

Computer plays a random simulation of a game on the board.

Computer picks a random number from the board and use that as the target value.

***Doing this allows the game to be unique every play but also ensures that they game is actually solvable in the first place**
