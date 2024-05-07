# https://leetcode.com/problems/rotate-image/description/
'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 
bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
'''


def rotate_using_space(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = matrix[n-j-1][i] 
    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]

def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - 1 - first
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
            

    
