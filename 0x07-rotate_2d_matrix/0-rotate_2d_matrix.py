#!/usr/bin/python3
'''Given an n X n 2D matrix, rotate it 90 degress clockwise'''


def rotate_2d_matrix(matrix):
    '''Rotate 2D matrix 90 degrees clockwise'''
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    length = len(matrix)
    new2dlist = []

    for t in range(length):
        newlist = []
        for a in range(length, 0, -1):
            newlist.append(matrix[a - 1][t])
        new2dlist.append(newlist)

    matrix[:] = list(new2dlist)
