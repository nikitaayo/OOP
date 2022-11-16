from enum import Enum


class Matrix:
    def __init__(self):
        self.size = 0

        self.key = None
        self.obj = None


class MatrixType(Enum):
    two_dimensional_array = 1
    diagonal = 2


class TwoDimArray:
    def __init__(self):
        self.data = []


class Diagonal:
    def __init__(self):
        self.data = None


def matrix_read_from(stream, line):
    k = int(line)

    matrix = Matrix()
    matrix.size = int(stream.readline().rstrip('\n'))

    if k == 1:
        matrix.key = MatrixType.two_dimensional_array
        matrix.obj = TwoDimArray()
        two_dimensional_array_read_from(matrix.obj, stream, matrix.size)
    elif k == 2:
        matrix.key = MatrixType.diagonal
        matrix.obj = Diagonal()
        diagonal_read_from(matrix.obj, stream)
    else:
        return 0

    return matrix


def matrix_write_to(matrix, stream):
    if matrix.key == MatrixType.two_dimensional_array:
        stream.write(f'\tThis is two-dimensional array\n')
        two_dimensional_array_write_to(matrix.obj, stream)
    elif matrix.key == MatrixType.diagonal:
        stream.write(f'\tThis is diagonal matrix\n')
        diagonal_write_to(matrix.obj, stream)
    else:
        stream.write('Error type\n')

    stream.write(f'\tSize: {matrix.size}\n')


def two_dimensional_array_read_from(matrix, stream, size):
    for i in range(size):
        line = stream.readline().rstrip('\n')
        matrix.data.append(list(map(lambda x: int(x), line.split())))

def two_dimensional_array_write_to(matrix, stream):
    for row in matrix.data:
        stream.write(f'\t\t{row}\n')


def diagonal_read_from(matrix, stream):
    matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

def diagonal_write_to(matrix, stream):
    stream.write(f'\t\t{matrix.data}\n')


def compare(first, second):
    return matrix_sum(first) < matrix_sum(second)


def matrix_sum(matrix):
    s = 0
    for item in matrix.obj.data:
        if isinstance(item, int):
            s += item
        else:
            s += sum(item)
    return s