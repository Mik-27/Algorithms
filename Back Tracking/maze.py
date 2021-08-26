"""
    A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down. 
    Find path for the rat in the maze to reach destination.
"""

# Utility dunction to find if the cell can be accessed.
def isSafe(maze, N, x, y):
    """
        Utility dunction to find if the cell can be accessed.
        Args:
            maze - Array for the maze
            N - length of array
            x - position in row
            y - position in column

        Returns true if the cell is safe/can be accessed.
    """

    if x >= 0 and y >= 0 and x < N and y < N and maze[x][y] == 1:
        return True

    return False


def rat_in_maze(maze):
    """
        This function solves the Maze problem using Backtracking.
        It mainly uses solveMazeUtil() to solve the problem. It
        returns false if no path is possible, otherwise return
        true and prints the path in the form of 1s.
    """

    N = len(maze)
    sol = [ [0 for j in range(N)] for i in range(N) ]

    if rat_util(maze, N, 0, 0, sol) == False:
        print("No feasible solution to given maze.")
        return False

    print(sol)
    return True


def rat_util(maze, N, x, y, sol):
    """
        Utility function to be called recursively to check next step to be
        taken in order to reach the destination.
    """

    if x == N-1 and y == N-1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if isSafe(maze, N, x, y):
        if sol[x][y] == 1:
            return False

        # Mark visited space/cell
        sol[x][y] = 1

        # Check each direction (top, bottom, left, right) for nest step
        if rat_util(maze, N, x+1, y, sol):
            return True
        if rat_util(maze, N, x-1, y, sol):
            return True
        if rat_util(maze, N, x, y+1, sol):
            return True
        if rat_util(maze, N, x, y-1, sol):
            return True

        # No space to move further
        sol[x][y] == 0
        return False


# Time Complexity: O(2^(n^2))