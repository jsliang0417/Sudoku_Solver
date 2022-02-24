# Sudoku_Solver
Sudoku Solver Project

1. forward_checking.py - backtracking and forward checking
1. AC3.py - arc consistency algorithm
1. Utility.py - supporting functions
1. Sudoku_solver.py - Take initial_S as input and return solution_S based on users' preference on choosing Backtracking + Forward Checking algorithm or Arc Consistency


# Usage

1. Run following command to install one module:
```python
    pip3 install -r requirements.txt
```

2. Run Sudoku_solver.py by typing following command in terminal:

    1. If you want to use AC3 Algorithm to solve your sudoku, then run:
    ```python
        python3 Sudoku_solver.py --method ac3 --input_file test.txt
    ```

    2. If you want to use Backtracking + Forward Checking Algorithm to solve your sudoku, then run:
    ```python
        python3 Sudoku_solver.py --method backtracking --input_file test.txt
    ```


3. Remarks: If you choose AC3 as your preferred algorithm, there is a chance that this algorithm may not return a fully solved sudoku. The code will immediately solve the unsolved sudoku with Backtracking + Forward Checking algorithm.


4. Code reference cited: [Aima-python: csp.py](https://github.com/aimacode/aima-python/blob/master/csp.py)