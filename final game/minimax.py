import wincheck as wc
import bestMove as bm
import numpy as np
cache = {}

# Getting all empty positions on board
def get_legal_moves(board):
    b = np.asarray(board)
    a, c = np.where(b == '_')
    legal_moves = np.array(list(zip(a, c)))
    return legal_moves


def minimax(board, depth, ism, alpha, beta, target_len):

    score = wc.win_check(board, target_len) # Checking if Winner or Draw
    legal_moves = get_legal_moves(board)

    if (depth > 4): # Depth huiristic
        return -100

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if len(legal_moves) == 0:
        return 0

    if (ism):

        # Maximising move
        best = -1000
        for i in range(0, len(legal_moves)):
            curr_move = legal_moves[i]
            board[curr_move[0], curr_move[1]] = bm.team_A
            best = max(best, minimax(board, depth + 1, not ism, alpha, beta,target_len))
            alpha = max(alpha, best)
            board[curr_move[0], curr_move[1]] = '_'
            if (alpha >= beta):
                break
        return best
    else:

        # Minimising opponent move
        best = 1000
        for i in range(0, len(legal_moves)):
            curr_move = legal_moves[i]
            board[curr_move[0], curr_move[1]] = bm.team_B
            best = min(best, minimax(board, depth + 1, not ism, alpha, beta,target_len))
            beta = min(beta, best)
            board[curr_move[0], curr_move[1]] = '_'
            if (alpha >= beta):
                break
        return best

# Only calculate a score if the board is not already in our cache.
def minimax_score_with_cache(board, depth, ism, alpha, beta, target_len):
    board_cache_key = str(board)
    if board_cache_key not in cache:
        best = minimax(board, depth, ism, alpha, beta, target_len)
        cache[board_cache_key] = best
        # f = open("boardcache.pkl", "a")
        # pickle.dump(cache[board_cache_key], f)
        # f.close()
    return cache[board_cache_key]
