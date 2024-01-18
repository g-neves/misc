#!/usr/bin/env python3

from typing import List, Tuple


directions = [
    [-1, 0], # Up
    [1, 0], # Down
    [0, -1], # Left
    [0, 1] # Right
]

def walk(maze: List[str], wall: str, curr: Tuple[int, int], end: Tuple[int, int], memo: set, path: List[Tuple[int, int]]) -> bool:
    # Base cases
    # 0. Out of bound
    if curr[0] < 0 or curr[0] >= len(maze) or curr[1] < 0 or curr[1] >= len(maze[0]):
        return False

    # 1. Hit a wall
    if maze[curr[0]][curr[1]] == wall:
        return False

    # 2. Got to the end
    if curr[0] == end[0] and curr[1] == end[1]:
        path.append(end)
        return True 

    # 3. Had already passed here
    if curr in memo:
        return False

    # Pre processing
    path.append(curr)
    memo.add(curr)

    # Recursion
    for direction in directions:
        new_curr = (curr[0] + direction[0], curr[1] + direction[1])
        if walk(
            maze=maze, 
            wall=wall, 
            curr=new_curr,
            end=end,
            memo=memo,
            path=path
            ):
            return True 

    # Post processing
    path.pop(-1)

    return False

def solve(maze: List[str], wall: str, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    path = []
    walk(maze, wall, start, end, set(), path) 

    return path

def get_start_and_end(maze: List[str]) -> Tuple[Tuple[int, int] | None, Tuple[int, int] | None]:
    start, end = None, None

    for x, line in enumerate(maze):
        for y, char in enumerate(line):
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)

    return (start, end)

def print_maze(maze: List[str]) -> None:
    maze_width = len(maze[0])

    print("", "-" * maze_width)
    for line in maze:
        print("|", end="")
        print(line, end="")
        print("|")

    print("", "-" * maze_width)

def print_solved_maze(maze: List[str], path: List[Tuple[int, int]]) -> None:
    solved_maze = maze.copy()
    for step in path:
        x = step[0]
        y = step[1]
        solved_maze[x] = solved_maze[x][:y] + "*" + solved_maze[x][y+1:]
        
    print_maze(solved_maze)
        


if __name__ == "__main__":
    maze = [
        "S######",
        " #     ",
        " #     ",
        " #     ",
        " ##### ",
        "       ",
        "###### ",
        "       ",
        "######E",
    ]

    start, end = get_start_and_end(maze)

    path = solve(maze, "#", start, end)

    print("Maze")
    print_maze(maze)
    print("Solution")
    print_solved_maze(maze, path)
