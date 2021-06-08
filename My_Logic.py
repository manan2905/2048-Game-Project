import random


def start_game():
    mat = [[0 for i in range(4)] for j in range(4)]
    return mat


def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    if mat[r][c] == 0:
        mat[r][c] = 2
    else:
        add_new_2(mat)


def check_status(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON!!!'

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'Game Not Over!'

    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i + 1][j]:
                return 'Game Not Over!'

    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'Game Not Over!'

    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'Game Not Over!'

    return 'Lost!'


def compress(mat):
    # changed = False  # to look at the changed variable
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        col_for_new = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][col_for_new] = mat[i][j]
                col_for_new += 1
    if mat == new_mat:
        return new_mat, False
    return new_mat, True


def merge(mat):
    changed = False  # to look at the changed variable
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1]:
                mat[i][j] = mat[i][j] + mat[i][j + 1]
                mat[i][j + 1] = 0
                changed = True

    return mat, changed


def transpose(mat):
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[j][i] = mat[i][j]
    return new_mat


def reverse(mat):
    new_mat = []
    for li in mat:
        new_mat.append(li[::-1])

    return new_mat


def move_left(mat):
    compressed_mat, changed1 = compress(mat)
    merged_mat, changed2 = merge(compressed_mat)
    changed = changed1 or changed2
    compressed_mat, temp = compress(merged_mat)
    return compressed_mat, changed


def move_up(mat):
    transposed_mat = transpose(mat)
    mat, changed = move_left(transposed_mat)
    transposed_mat = transpose(mat)
    return transposed_mat, changed


def move_right(mat):
    reveresed_mat = reverse(mat)
    mat, changed = move_left(reveresed_mat)
    reveresed_mat = reverse(mat)
    return reveresed_mat, changed


def move_down(mat):
    transposed_mat = transpose(mat)
    mat, changed = move_right(transposed_mat)
    transposed_mat = transpose(mat)
    return transposed_mat, changed


def print_mat(mat):
    for li in mat:
        print(li)
