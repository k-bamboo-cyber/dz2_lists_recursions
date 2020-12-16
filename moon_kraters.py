"""поиск кратеров."""
from typing import Any


def calculate(mat: list) -> int:
    """функция возвращает кол-во кратеров."""
    if mat is None or len(mat) == 0:
        return 0
    res = 0
    i = 0
    while i < len(mat):
        j = 0
        while j < len(mat[i]):
            if mat[i][j] == 1:
                res += 1
                check(mat, i, j)
            j += 1
        i += 1
    return res


def check(mat: list, row: int, col: int) -> Any:
    """функция для проверки соседних цифр."""
    if row < 0 or col < 0 or row >= len(mat) or col >= len(mat[0]) or mat[row][col] == 0:
        return
    mat[row][col] = 0
    r = [-1, 0, 1, 0]
    c = [0, 1, 0, -1]
    i = 0
    while i < len(r):
        check(mat, row + r[i], col + c[i])
        i += 1


def file_reading(file: str) -> list:
    """функция для чтения файла."""
    f = open(file, 'r')
    d = list()
    for line in f:
        m = line.replace('\n', "").split()
        j = 0
        for i in m:
            m[j] = int(i)
            j += 1
        d.append(m)
    f.close()
    return d


data = file_reading('input.txt')

count = calculate(data)
print("Число кратеров:", count)
