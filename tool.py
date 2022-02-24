def convert_grid_to_string(grid):
    decompose = [j for i in grid for j in i]
    strings_to_integer = [str(i) for i in decompose]
    for i in range(len(strings_to_integer)):
        if strings_to_integer[i] == '0':
            strings_to_integer[i] = '.'
    return("".join(strings_to_integer))


sample_sudoku = [
        [0, 5, 0, 0, 7, 0, 0, 0, 1], 
        [8, 7, 6, 0, 2, 1, 9, 0, 3], 
        [0, 0, 0, 0, 3, 5, 0, 0, 0], 
        [0, 0, 0, 0, 4, 3, 6, 1, 0], 
        [0, 4, 0, 0, 0, 9, 0, 0, 2], 
        [0, 1, 2, 0, 5, 0, 0, 0, 4], 
        [0, 8, 9, 0, 6, 4, 0, 0, 0], 
        [0, 0, 0, 0, 0, 7, 0, 0, 0], 
        [1, 6, 7, 0, 0, 2, 5, 4, 0]]



print(convert_grid_to_string(sample_sudoku))



"""
input: 
[
        [0, 5, 0, 0, 7, 0, 0, 0, 1], 
        [8, 7, 6, 0, 2, 1, 9, 0, 3], 
        [0, 0, 0, 0, 3, 5, 0, 0, 0], 
        [0, 0, 0, 0, 4, 3, 6, 1, 0], 
        [0, 4, 0, 0, 0, 9, 0, 0, 2], 
        [0, 1, 2, 0, 5, 0, 0, 0, 4], 
        [0, 8, 9, 0, 6, 4, 0, 0, 0], 
        [0, 0, 0, 0, 0, 7, 0, 0, 0], 
        [1, 6, 7, 0, 0, 2, 5, 4, 0]
]

output:
.5..7...1876.219.3....35.......4361..4...9..2.12.5...4.89.64........7...167..254.
"""