def convertToString(grid):
    flattenList = [j for sub in grid for j in sub]
    string_ints = [str(int) for int in flattenList]
    for i in range(len(string_ints)-1):
        if string_ints[i] == '0':
            string_ints[i] = '.'
    return("".join(string_ints))



grid = [[8, 7, 0, 0, 0, 0, 6, 5, 2], [0, 0, 0, 0, 7, 2, 4, 0, 0], [0, 3, 2, 0, 5, 0, 0, 0, 0], [0, 0, 8, 0, 0, 5, 3, 0, 4], [6, 0, 0, 9, 0, 3, 0, 0, 0], [0, 1, 3, 7, 0, 0, 0, 0, 0], [5, 0, 9, 4, 0, 7, 0, 0, 0], [3, 0, 0, 1, 0, 9, 0, 7, 0], [1, 2, 0, 0, 0, 6, 0, 4, 9]]









print(convertToString(grid))