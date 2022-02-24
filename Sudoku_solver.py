from AC3 import Sudoku
from AC3 import AC3, AC3b, AC4
from AC3 import backtracking_search, mrv, forward_checking
import time
import argparse

easy1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
harder1 = '4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
test_case_1 = '5346789..672195348198342567859761423426853791713924856961537284287419635345286179'

t4 = '.5..7...1876.219.3....35.......4361..4...9..2.12.5...4.89.64........7...167..254.'


def ac3_algo(input):
    solution = Sudoku(input)
    print("Sudoku to be solved:")
    solution.display(solution.infer_assignment())
    print("------------------------------")
    start = time.time()
    AC3(solution)
    end = start - time.time()
    solution.display(solution.infer_assignment())


def backtracking_algo(input):
    solution = Sudoku(input)
    print("Sudoku to be solved:")
    solution.display(solution.infer_assignment())
    print("------------------------------")
    start = time.time()
    backtracking_search(solution, select_unassigned_variable=mrv, inference=forward_checking)
    end = start - time.time()
    solution.display(solution.infer_assignment())
    
    


#parse argument
parser = argparse.ArgumentParser()
parser.add_argument("--method", help="ac3 or backtracking+forward checking")
parser.add_argument("--input_file", help="input your test file for this argument")
args = parser.parse_args()

if args.method == "ac3":
    if args.input_file == "input.txt":
        print("Solving input.txt with AC3 algorithm.")
        ac3_algo(t4)
elif args.method == "backtracking":
    if args.input_file == "input.txt":
        print("Solving input.txt with Backtracking algorithm.")
        backtracking_algo(t4)
        