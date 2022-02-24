# Sudoku Solver
Sudoku Solver Project

1. AC3.py - arc consistency algorithm
1. Utility.py - supporting functions
1. Sudoku_solver.py - Take initial_S as input and return solution_S based on users' preference on choosing Backtracking + Forward Checking algorithm or Arc Consistency. If AC3 algorithm returns unsolved sudoku, Backtracking + Forward Checking algorithm will try to solve the unsolved sudoku.


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


3. If you want to input your own unsolved sudoku, you will need to copy and paste your unsolved sudoku into tool.py to convert your unsolved sudoku to an acceptable format by running this command after you pasted the unsolved sudoku into tool.py:
```python
    python3 tool.py
```
After converting, you will need to copy and paste the convered version of unsolved sudoku into test.txt file.

4. Remarks: If you choose AC3 as your preferred algorithm, there is a chance that this algorithm may not return a fully solved sudoku. The code will immediately solve the unsolved sudoku with Backtracking + Forward Checking algorithm.



# Acknowledgements

Thank you for the repo [Aima-python: csp.py](https://github.com/aimacode/aima-python/blob/master/csp.py)   
Code reference cited: [Aima-python: csp.py](https://github.com/aimacode/aima-python/blob/master/csp.py)
