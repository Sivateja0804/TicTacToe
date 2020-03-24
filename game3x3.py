class Game:
    row = 0
    col = 0

team_A = 'x'
team_B = 'o'

def move_count(board):
    for i in range(0,3):
        for j in range(0,3):
            if (board[i][j] == '_'):
                return True
    return False

def win_check(b):
    # Checking for Rows for X or O victory
        for row in range(0,3):
            if b[row][0]==b[row][1] and b[row][1]==b[row][2]:
                if b[row][0] == team_A:
                    return +10
                elif b[row][0] == team_B:
                    return -10

    # Checking for Col for X or O victory
        for col in range(0,3):
            if b[0][col]==b[1][col] and b[1][col]==b[2][col]:
                if b[0][col] == team_A:
                    return +10
                elif b[0][col] == team_B:
                    return -10

    # Checking for Diagonals for X or O victory
        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
            if b[0][0] == team_A:
                return +10
            elif b[0][0] == team_B:
                return -10


        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
            if b[0][2] == team_A:
                return +10
            elif b[0][2] == team_B:
                return -10

def minimax(board,depth,ism):
    score = win_check(board)
    if score == 10:
        return score-depth

    if score == -10:
        return score+depth

    if move_count(board) == False:
        return 0

    if (ism):
        best = -1000
        for i in range(0, 3):
            for j in range(0, 3):
                if (board[i][j] == '_'):
                    board[i][j] = team_A
                    best = max(best, minimax(board,depth + 1, not ism))
                    board[i][j] = '_'

        return best
    else:
        best = 1000
        for i in range(0, 3):
            for j in range(0, 3):
                if (board[i][j] == '_'):
                    board[i][j] = team_B
                    best = min(best, minimax(board, depth + 1, not ism))
                    board[i][j] = '_'
        return best

def fb_move(board):
    bestVal = -1000
    bestMove = Game()
    bestMove.row = -1
    bestMove.col = -1
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == '_'):
                board[i][j] = team_A
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if moveVal>bestVal:
                    bestMove.row = i
                    bestMove.col = j
                    bestVal = moveVal
    return bestMove.row,bestMove.col

if __name__ == '__main__':
    board = [['x', 'o', 'x'],
             ['o', 'o', 'x'],
             ['_', '_', '_']]

    row,col = fb_move(board);
    print(row,col)