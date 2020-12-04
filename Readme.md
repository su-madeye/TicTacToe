# Tic Tac Toe
## About the game

This is a replica of the classic game of Tic Tac Toe where two players try to mark 3 continuous squares on a 3*3 grid. The game is completely built on python using the pygame library. The game starts with **`Player 1`** or **`Player X`** marking his square on the grid followed by **`Player 2`** or **`Player O`** doing the same. This is continued until a player wins or there is no more space on the grid to put the markers on. That is the game ends when a player wins or all the squares are filled (9 moves in totoal). As the game ends, a message is displayed with the winner (or a message stating that it is a tie). The game then resets allowing players to play the next round.

## How to play

+ Download the tictactoe.py file in the required workspace.
+ Open a terminal window in the workspace.
+ Run **`python3 tictactoe.py`** command to fireup the game.
+ Using left mouse clicks, the players can mark their squares with either **`X`** or **`O`**.
+ When a player wins according to the classic Tic Tac Toe rules, the game finishes showing the player who won the round.
+ In case of a tie, the round again comes to an end displaying that the round ended.
+ After a couple of seconds, the board automatically resets and a new round starts.

Note: Make sure to have python3 installed on your machine. In case you do not have python3 or the pygame library, use
 + [Click here](https://phoenixnap.com/kb/how-to-install-python-3-windows) to install python on your windows pc.
 + `pip install pygame` command to install pygame library

## Workflow

+ With each round, the board resets providing a fresh grid to the players to play.
+ The **`Player 1`** or **`Player X`** starts the game by choosing a square on the grid and marking it with **`X`**.
+ The **`Player 2`** now choose his square from all the unmarked squares on the grid and marks it with **`O`**
+ The game comes to an end when a player wins or when the game draws.
+ At the end of the game, the winner is displayed.
+ The board then resets to start the next round.

## Function Breakdown:

The following user-defined functions have been implemented in the game.

+ **`check_game_over()`**: The funtion is used to determine if the game is over or not. It is done by acknowledging the fact that game ends when a player wins and when there are no more empty squares available on grid. 
+ **`draw_board(i)`**: The function is used to draw the grid on the screen. It has a parameter `i` which is used for animation purpose.
+ **`draw_marker(row, col, player)`**: After a player makes a valid move, this function is called to mark the square in which the player clicks. The parameters `row` and `col`  are used to determine the square on which the player wishes to put his marker and parameter `player` determines which player is putting the marker.
+ **`draw_markers()`**: It is an extension of the function `draw_marker(row, col, player)` which makes sure that the required markers are always displayed.
+ **`get_grid_pos(x,y)`**: The funtion returns the square in terms of `row` and `col` in which the player haas clicked. 
+ **`get_game_over(winner)`**: The function displays the end result of the game and call `reset_grid` to reset the game for the next round.
+ **`in_rect(x,y)`**: The function checks if the player has clicked in the grid or not. It returns `True` if the player has clicked within the grid otherwise `False`. The parameters `x` & `y` are the position where the player has clicked.
+ **`reset_grid()`**: The functions is used to reset the grid after a round ends. It is executed when a new round starts.



