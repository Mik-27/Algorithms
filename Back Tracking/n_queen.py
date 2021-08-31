# N Queen Algorithm using Backtracking

global N
N = 4

def is_safe(board, row, col):
    """
        Function to check if the queen can be placed at given position
        safely.
        Args:
            board - 2d array containing the info about placed queens
            row, col - index of row and column to be checked.
        Returns True if placing is safe.
    """

    # ---Q
    for i in range(col):
        if board[row][i] == 1:
            return False
    # \
    #  \
    #   Q
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    #   Q
    #  /
    # /
    for i,j in zip(range(row,N,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True

def nqueen_util(board,col):
    """
        Function to recursively check for eacch column and place the queen in 
        the safe position
        Args:
            board - 2D array with position of queens
            col - index for column to be iterated

    """

    if col > N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] == 1

            if nqueen_util(board, col+1):
                return True

            # Backtracking
            board[i][col] = 0

    return False


def nqueen(board):
    if not nqueen_util(board, 0):
        print("Solution does not exist.")
        return False

    print(board)
    return True


# Time Complexity: O(N!)