from AC3 import Sudoku
from AC3 import *
import argparse

#parse argument
parser = argparse.ArgumentParser()
parser.add_argument("--method", help="ac3 or backtracking+forward checking")
parser.add_argument("--input_file", help="input your test file for this argument")
args = parser.parse_args()



def sudoku_quantity():
    file = open(args.input_file, 'r')
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    line_count = len(nonempty_lines)
    file.close()

    print(line_count)
    return line_count


def fetch_unsolved_sudoku():
    unsolved_list = [line.rstrip() for line in open('test.txt', 'r')]
    return unsolved_list



def ac3_algo(input):
    solution = Sudoku(input)
    print("Sudoku to be solved with AC3:")
    solution.display(solution.infer_assignment())
    AC3(solution)
    print("--------------------------------------------")
    solution.display(solution.infer_assignment())

    
    length = [len(value) for key, value in solution.return_curr_domains().items()]
    if length[0] >= 1:
        print("AC3 failed to solve, trying Backtracking: ")
        backtracking_algo(input)


def backtracking_algo(input):
    solution = Sudoku(input)
    print("Sudoku to be solved with backtracking:")
    solution.display(solution.infer_assignment())
    print("--------------------------------------------")
    backtracking_search(solution, select_unassigned_variable=mrv, inference=forward_checking)
    solution.display(solution.infer_assignment())
    

if args.method == "ac3":
    if args.input_file == "test.txt":
        print("Solving input.txt with AC3 algorithm.")
        for i in range(sudoku_quantity()):
            ac3_algo(fetch_unsolved_sudoku()[i])
        
elif args.method == "backtracking":
    if args.input_file == "test.txt":
        print("Solving input.txt with Backtracking algorithm.")
        for i in range(sudoku_quantity()):
            backtracking_algo(fetch_unsolved_sudoku()[i])