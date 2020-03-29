import sys
import time
import numpy as np
import pickle

class Game:
    row = 0
    col = 0

team_A = 'o'
team_B = 'x'
cache = {}

def get_legal_moves(board):
    b = np.asarray(board)
    a, c = np.where(b == '_')
    legal_moves = np.array(list(zip(a, c)))
    return legal_moves


def win_check(b):
    # Checking for Rows for X or O victory
        for row in range(0,4):
            if b[row][0]==b[row][1] and b[row][1]==b[row][2] and b[row][2]== b[row][3]:
                if b[row][0] == team_A:
                    return +10
                elif b[row][0] == team_B:
                    return -10

    # Checking for Col for X or O victory
        for col in range(0,4):
            if b[0][col] == b[1][col] and b[1][col] == b[2][col] and b[2][col] == b[3][col]:
                if b[0][col] == team_A:
                    return +10
                elif b[0][col] == team_B:
                    return -10

    # Checking for Diagonals for X or O victory
        if b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[3][3] == b[2][2]:
            if b[0][0] == team_A:
                return +10
            elif b[0][0] == team_B:
                return -10


        if b[0][3] == b[1][2] and b[1][2] == b[2][1] and b[2][1] == b[3][0]:
            if b[0][2] == team_A:
                return +10
            elif b[0][2] == team_B:
                return -10

def minimax(board,depth,ism,alpha,beta):
    score = win_check(board)
    legal_moves = get_legal_moves(board)

    if (depth > 8):
        return -100
    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if len(legal_moves) == 0:
        return 0

    if (ism):
        best = -1000
        for i in range(0, len(legal_moves)):
            curr_move = legal_moves[i]
            board[curr_move[0],curr_move[1]] = team_A
            best = max(best, minimax(board, depth + 1, not ism, alpha, beta))
            alpha = max(alpha, best)
            board[curr_move[0],curr_move[1]] = '_'
            if (alpha >= beta):
                break
        return best
    else:
        best = 1000
        for i in range(0, len(legal_moves)):
            curr_move = legal_moves[i]
            board[curr_move[0],curr_move[1]] = team_B
            best = min(best, minimax(board, depth + 1, not ism, alpha, beta))
            beta = min(beta, best)
            board[curr_move[0],curr_move[1]] = '_'
            if (alpha >= beta):
                break
        return best

def minimax_score_with_cache(board,depth,ism,alpha,beta):
    board_cache_key = str(board)
    if board_cache_key not in cache:
        best = minimax(board, depth, ism,alpha,beta)
        cache[board_cache_key] = best
        # f = open("boardcache.pkl", "a")
        # pickle.dump(cache[board_cache_key], f)
        # f.close()
    return cache[board_cache_key]


def fb_move(board,alpha,beta):
    bestVal = -1000
    bestMove = Game()
    bestMove.row = -1
    bestMove.col = -1
    for i in range(0, 4):
        for j in range(0, 4):
            if (board[i][j] == '_'):
                board[i][j] = team_A
                moveVal = minimax_score_with_cache(board, 0, False,alpha,beta)
                #moveVal = minimax(board, 0, False,alpha,beta)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove.row = i
                    bestMove.col = j
                    bestVal = moveVal
    return bestMove.row,bestMove.col

if __name__ == '__main__':
    # board = [['x', 'o', 'o'],
    #          ['x', '_', '_'],
    #          ['X', '_', '_']]

    board = [['_', '_', '_', '_'],
             ['_', '_', '_', '_'],
             ['_', '_', '_', '_'],
             ['_', '_', '_', '_']]
    # board = [['_', '_', '_', '_','_', '_', '_', '_','_', '_', '_', '_'],
    #          ['_', '_', '_', '_','_', '_', '_', '_','_', '_', '_', '_'],
    #          ['_', '_', '_', '_','_', '_', '_', '_','_', '_', '_', '_'],
    #          ['_', '_', '_', '_','_', '_', '_', '_','_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ],
    #          ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' ]
    #          ]
    b = np.asarray(board)
    #print(b)
    alpha = -sys.maxsize
    beta = sys.maxsize
    start = time.time()
    row,col = fb_move(b,alpha,beta)
    end = time.time()
    print(end-start)
    print(row,col)

