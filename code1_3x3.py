class Game:
    row = 0
    col = 0

team_A = 'x'
team_B = 'o'

def move_count(board):
    for i in range(0,len(board[0])):
        for j in range(0,len(board[0])):
            if (board[i][j] == '_'):
                return True
    return False

def win_check(b):
    # Checking for Rows for X or O victory
    res = False
    for row in range(0, len(b[0])):
        res = all(ele == b[row][0] for ele in b[row])
        if res:
            if b[row][0] == team_A:
                return +10
            elif b[row][0] == team_B:
                return -10

    # Checking for Col for X or O victory
        for col in range(0,len(b[0])):
            res = all(ele == b[0][col] for ele in [row[col] for row in b])
            if res:
                if b[0][col] == team_A:
                    return +10
                elif b[0][col] == team_B:
                    return -10

    # Checking for Diagonals for X or O victory
    li = []
    for col in range(0, len(b[0])):
        li.append(b[col][col])
    res = all(ele == b[0][0] for ele in li)
    if res:
        if b[0][0] == team_A:
            return +10
        elif b[0][0] == team_B:
            return -10

    li = []
    end = len(b[0]) - 1
    for col in range(0, len(b[0])):
        li.append(b[col][end])
        end -= 1
    res = all(ele == b[0][len(b[0]) - 1] for ele in li)
    if res:
        if b[0][3] == team_A:
            return +10
        elif b[0][3] == team_B:
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
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if (board[i][j] == '_'):
                    board[i][j] = team_A
                    best = max(best, minimax(board,depth + 1, not ism))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(0, len(board)):
            for j in range(0, len(board)):
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
    for i in range(0, len(board)):
        for j in range(0, len(board)):
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
    board = [['x', 'o', 'o','x'],
             ['x', 'x', 'o','x'],
             ['_', '_', 'x','_'],
             ['_', '_', '_','_']]
    row,col = fb_move(board)
    print(row,col)