'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to 0. 
'''

# store rows and cols which need to be null
def zero_matrix(matrix : list[list[int]]):
    # we can also use boolean array
    null_rows = set()
    null_cols = set()
    rows = len(matrix)
    cols = len(matrix[0])
    

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                null_rows.add(i)
                null_cols.add(j)

    for r in null_rows:
        for j in range(cols):
            matrix[r][j] = 0
    for c in null_cols:
        for i in range(rows):
            matrix[i][c] = 0
    return None


matrix = [[1,1,1],[1,0,0],[1,1,1]]
zero_matrix(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])


