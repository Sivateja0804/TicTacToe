import bestMove as bm
import time
import numpy as np
import sys
import API.GetBoardAPI as gb
import API.GetMoveAPI as gm
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

def check_turn(gameId):
    data = gm.get_prev_move(gameId)
    data = json.loads(data)
    return data["moves"][0]["teamId"]

# This is the main method we call and returns i,j index for the matrix
if __name__ == '__main__':
    startTime = time.time()
    gameId="763"
    opponent_teamid = "1197"
    board, target = get_board("0,4", gameId)
    if np.all(board == board[0,:]):
        mmv.make_a_move(str(5) + "," + str(5), gameId)
    else:
        alpha = -sys.maxsize
        beta = sys.maxsize
        while(True):
            last_move = check_turn(gameId)
            if last_move == opponent_teamid :
                row, col = bm.find_best_move(board, alpha, beta, target)
                end = time.time()
                print(end - startTime)
                print(row, col)
                data = mmv.make_a_move(str(row) + "," + str(col), gameId)
                board, target = get_board("0,4", gameId)
                print(board)
                data = json.loads(data)
                if data["message"] == "Cannot make move - Game is no longer open: " + gameId + "":
                    break
