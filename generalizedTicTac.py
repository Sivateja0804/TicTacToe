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


def win_check(board, win_row):
    a = team_A * win_row
    b = team_B * win_row

    # Checking for Rows for X or O victory
    for row in range(0, len(board)):
        full_row = "".join(board[row])
        if a in full_row:
            return +10
        elif b in full_row:
            return -10

    # Checking for Col for X or O victory
    for col in range(0, len(board)):
        full_col = "".join(board[:, col])
        if a in full_col:
            return +10
        elif b in full_col:
            return -10

    # Checking for Diagonals for X or O victory
    diag = "".join(board.diagonal())
    rev_diag = "".join(np.diag(np.fliplr(board)))
    if a in diag or a in rev_diag:
        return 10
    elif a in diag or a in rev_diag:
        return -10

    # checking all other possible diagonals for sub matrices
    l = len(board) - 3
    for i in range(4, len(board) + 1):
        matrix1_diagonal = "".join(board[:i, l:].diagonal())
        matrix2_diagonal = "".join(board[l:, :i - 1].diagonal())

        # 3 and 4 we need opposite diagonal
        matrix3_diagonal = "".join(np.diag(np.fliplr(board[:i - 1, :i - 1])))
        matrix4_diagonal = "".join(np.diag(np.fliplr(board[l:, l:])))
        if a in matrix1_diagonal or a in matrix2_diagonal or a in matrix3_diagonal or a in matrix4_diagonal:
            return 10
        elif b in matrix1_diagonal or b in matrix2_diagonal or b in matrix3_diagonal or b in matrix4_diagonal:
            return -10
        l -= 1


def minimax(board, depth, ism, alpha, beta, win_row):
    score = win_check(board, win_row)
    legal_moves = get_legal_moves(board)

    if (depth > 4):
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
            board[curr_move[0], curr_move[1]] = team_A
            best = max(best, minimax(board, depth + 1, not ism, alpha, beta,win_row))
            alpha = max(alpha, best)
            board[curr_move[0], curr_move[1]] = '_'
            if (alpha >= beta):
                break
        return best
    else:
        best = 1000
        for i in range(0, len(legal_moves)):
            curr_move = legal_moves[i]
            board[curr_move[0], curr_move[1]] = team_B
            best = min(best, minimax(board, depth + 1, not ism, alpha, beta,win_row))
            beta = min(beta, best)
            board[curr_move[0], curr_move[1]] = '_'
            if (alpha >= beta):
                break
        return best


def minimax_score_with_cache(board, depth, ism, alpha, beta, win_row):
    board_cache_key = str(board)
    if board_cache_key not in cache:
        best = minimax(board, depth, ism, alpha, beta, win_row)
        cache[board_cache_key] = best
        # f = open("boardcache.pkl", "a")
        # pickle.dump(cache[board_cache_key], f)
        # f.close()
    return cache[board_cache_key]


# find the best move
def find_best_move(board, alpha, beta, win_row):
    bestVal = -1000
    bestMove = Game()
    bestMove.row = -1
    bestMove.col = -1
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if (board[i][j] == '_'):
                board[i][j] = team_A
                moveVal = minimax_score_with_cache(board, 0, False, alpha, beta, win_row)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove.row = i
                    bestMove.col = j
                    bestVal = moveVal
    return bestMove.row, bestMove.col


if __name__ == '__main__':
    startTime = time.time()
    rows = 4
    col = 4
    win_row = 4
    board = np.full((rows, col), "_")
    alpha = -sys.maxsize
    beta = sys.maxsize
    row, col = find_best_move(board, alpha, beta, win_row)
    end = time.time()
    print(end - startTime)
    print(row, col)
