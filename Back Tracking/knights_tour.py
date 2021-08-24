def isSafe(n, x, y, board):
    """
        A function to return whether the specific position is safe or not
        Args:
            x, y - Position in the chessboard
            board - 2d array for keeping track of visited cells and maintain 
                    the order in which they are visited

        Return True if the position of the cell is safe else False
    """

    if x>=0 and y>=0 and x<n and y<n and board[x][y] == -1:
        return True
    return False


def knights_tour(n):
    """
        A function to output the path followed by a chess knight to cover
        all the cells in a chessboard using backtracking.
        Args:
            n - n x n chessboard
    """

    # Initialize the chessboard with -1 viz. not visited
    board = [[-1 for i in range(n)] for j in range(n)]

    # Moves available for the knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Step counter for knight's position
    pos = 1

    # Initial Position
    board[0][0] = 0

    if not knights_tour_util(n, board, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
    else:
        print(board)


def knights_tour_util(n, board, cur_x, cur_y, move_x, move_y, pos):
    """
        Recursive utility function for solving the knights tour problem
        Args:
            cur_x, cur_y - Current position of x and y for the knight
    """

    if pos == n**2:
        return True

    for i in range(n):
        new_x = cur_x + move_x[i]
        new_y = cur_y + move_y[i]
        if isSafe(n, new_x, new_y, board):
            board[new_x][new_y] = pos
            if knights_tour_util(n, board, new_x, new_y, move_x, move_y, pos+1):
                return True

            board[new_x][new_y] = -1
    
    return False