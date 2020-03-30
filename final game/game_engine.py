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
    gameId="351"
    board,target=get_board("0,4", gameId)
    alpha = -sys.maxsize
    beta = sys.maxsize
    row, col = bm.find_best_move(board, alpha, beta, target)
    end = time.time()
    print(end - startTime)
    print(row, col)
    mmv.make_a_move(str(row)+","+str(col),gameId)

