# Tally_UP
Grid based math Game that you combine numbers together to reach a target sum.


# How to play the Game.
select a cell on the grid and combine it with one of its orthogonal / cardinal neighbours.

### Rules of the game

For numbers- add together, with the number selected first becoming empty and then replace with the default values contained in the set.

for number and operator- operator is placed at the front of the number i.e. 2 combined with x would become x2. if x2 and x4 are combined it will make a cell with value x8. 
- there will a limit up to x16.
  

# how the game works internally

Randomly generate a 4x4 cell with values contained in the set [0,1,2,3,-,*,mod,rem] <-- mod,rem and 0 are 50/50 right now.

randomly generate a list of next moves.

play a random simulation of a game on the board.

pick a random number from the board and use that as the target value.

***Doing this allows the game to be unique every play but also ensures that they game is actually solvable in the first place**
