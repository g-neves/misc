import argparse


def is_valid(board, row, col, n):
    # check for queens in the row
    for i in range(col):
        if board[row][i]:
            return False

    # upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # lower left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def print_solution(board, n):
    black_square = "□"
    white_square = "■"
    queen = "♕"
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print(queen, end=" ")
            else:
                if (i + j) % 2 == 0:
                    print(white_square, end=" ")
                else:
                    print(black_square, end=" ")
        print()

def solve(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1

            if solve(board, col+1, n):
                return True 

            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]

    if not solve(board, 0, n):
        print("Solution does not exist")
        return False

    print_solution(board, n)
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solves the n-queens problem for a nxn board")
    parser.add_argument("-n", "--N", help="Dimension of the board", default=8, type=int)
    args = parser.parse_args()
    solve_n_queens(args.N)
