import bestMove as bm
import time
import numpy as np
import sys
import API.GetBoardAPI as gb
import API.MakeAMoveAPI as mmv
import json

# this will return the current board details.
def get_board(move,gameId):
    data = gb.get_current_board(move, gameId)
    data = json.loads(data)
    rows = cols = 12
    board = np.full((rows, cols), "_")
    if data["output"]:
        board_data=json.loads(data["output"])
        # rows=cols=data["boardSize"]
        for k, v in board_data.items():
            board[int(k.split(",")[0]), int(k.split(",")[1])] = v
    target=data["target"]

    return board,target

# This is the main method we call and returns i,j index for the matrix
if __name__ == '__main__':
    startTime = time.time()
    gameId="763"
    board, target = get_board("0,4", gameId)
    if np.all(board == board[0,:]):
        mmv.make_a_move(str(5) + "," + str(5), gameId)
    else:
        board = [['_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_'],
         ['_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_'],
         ['_' '_' '_' '_' '_' 'X' '_' '_' '_' '_' '_' '_'],
         ['_' '_' '_' '_' 'O' 'O' '_' '_' '_' '_' '_' '_'],
         ['_' '_' 'O' 'O' 'X' 'O' 'O' 'O' '_' '_' '_' '_'],
         ['_' '_' 'O' 'X' 'X' 'O' 'X' '_' '_' '_' '_' '_'],
         ['_' '_' 'X' 'X' '_' 'X' 'X' 'X' 'O' '_' '_' '_'],
         ['_' '_' '_' '_' 'X' 'O' 'O' '_' '_' '_' '_' '_'],
         ['_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_'],
         ['_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_'],
         ['_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_'],
         ['_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_' '_']]
        board = np.asarray(board)
        alpha = -sys.maxsize
        beta = sys.maxsize
        row, col = bm.find_best_move(board, alpha, beta, 6)
        end = time.time()
        print(end - startTime)
        print(row, col)
        mmv.make_a_move(str(row)+","+str(col),gameId)
        board, target = get_board("0,4", gameId)
        print(board)
