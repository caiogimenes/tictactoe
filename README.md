# Tic Tac Toe Player

This repository provides an AI player for the classic game of Tic Tac Toe. The AI is implemented using the Minimax algorithm which explores all possible states of the board to determine the optimal move. The AI is unbeatable and will always play optimally to either win or draw the game.

## Dependencies

- Python 3.x
- The `runner.py` file from the [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2023/) course by Harvard University.

## Usage

1. Clone the repository to your local machine.
```bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

2. Ensure you have the `runner.py` file from the CS50 AI course in the same directory as the script.

3. Run the `runner.py` script using Python.
```bash
python runner.py
```

4. The `runner.py` script will initialize the game and the AI will play against you. Make your move by specifying the row and column number (both ranging from 0 to 2) when prompted.

## Code Overview

The Tic Tac Toe script contains several functions to handle the game logic, AI logic, and utility calculations.

- `initial_state()`: Returns the starting state of the board.
- `player(board)`: Returns the player who has the next turn on a board.
- `actions(board)`: Returns a set of all possible actions available on the board.
- `result(board, action)`: Returns the board that results from making a move on the board.
- `winner(board)`: Returns the winner of the game if there is one.
- `terminal(board)`: Returns True if the game is over, False otherwise.
- `utility(board)`: Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
- `minimax(board)`: Returns the optimal action for the current player on the board.

Here's a brief overview of the Minimax implementation in the `minimax` function:

```python
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    moves = actions(board)
    # Max player logic
    if player(board) == X:
        max_value = float('-inf')
        max_move = None
        for move in moves:
            state = result(board, move)
            while terminal(state) is False:
                state = result(state, minimax(state))
            score = utility(state)
            if score > max_value:
                max_value = score
                max_move = move
            if min(max_value, 1) == 1:
                return max_move
        return max_move
    
    # Min player logic
    if player(board) == O:
        min_value = float('inf')
        min_move = None
        for move in moves:
            state = result(board, move)
            while terminal(state) is False:
                state = result(state, minimax(state))
            score = utility(state)
            if score < min_value:
                min_value = score
                min_move = move
            if max(min_value, -1) == -1:
                return min_move
        return min_move
```

## License

[MIT](LICENSE)
