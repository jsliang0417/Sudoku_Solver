"""
Student: Steve Liang
ID: 010878575
Code Purpose: Utilize AC3 and Backtracking + Forward Checking algorithms to solve sudoku
Code Reference Cited: https://github.com/aimacode/aima-python/blob/master/csp.py
"""

def sudoku_quantity(file):
    file = open(file, 'r')
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    line_count = len(nonempty_lines)
    file.close()

    print(line_count)
    return line_count


def fetch_unsolved_sudoku(file):
    unsolved_list = [line.rstrip() for line in open(file, 'r')]
    return unsolved_list