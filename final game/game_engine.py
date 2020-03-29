import bestMove as bm
import time
import numpy as np
import sys

if __name__ == '__main__':
    startTime = time.time()
    rows = 3
    col = 3
    target_len = 3
    board = np.full((rows, col), "_")
    alpha = -sys.maxsize
    beta = sys.maxsize
    row, col = bm.find_best_move(board, alpha, beta, target_len)
    end = time.time()
    print(end - startTime)
    print(row, col)
