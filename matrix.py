from enum import Enum


class Matrix:
    def __init__(self):
        self.size = 0
        self.out_type = 0

        self.key = None
        self.obj = None


class MatrixType(Enum):
    two_dimensional_array = 1
    diagonal = 2
    triangle = 3


class TwoDimArray:
    def __init__(self):
        self.data = []


class Diagonal:
    def __init__(self):
        self.data = None


class Triangle:
    def __init__(self):
        self.data = []


def matrix_read_from(stream, line):
    k = int(line)

    matrix = Matrix()
    matrix.size = int(stream.readline().rstrip('\n'))
    matrix.out_type = int(stream.readline().rstrip('\n'))

    if k == 1:
        matrix.key = MatrixType.two_dimensional_array
        matrix.obj = TwoDimArray()
        two_dimensional_array_read_from(matrix.obj, stream, matrix.size)
    elif k == 2:
        matrix.key = MatrixType.diagonal
        matrix.obj = Diagonal()
        diagonal_read_from(matrix.obj, stream)
    elif k == 3:
        matrix.key = MatrixType.triangle
        matrix.obj = Triangle()
        triangle_read_from(matrix.obj, stream)
    else:
        return 0

    return matrix


def matrix_write_to(matrix, stream):
    if matrix.key == MatrixType.two_dimensional_array:
        stream.write(f'\tThis is two-dimensional array\n')
        two_dimensional_array_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
    elif matrix.key == MatrixType.diagonal:
        stream.write(f'\tThis is diagonal matrix\n')
        diagonal_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
    elif matrix.key == MatrixType.triangle:
        stream.write('\tThis is triangle matrix\n')
        triangle_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
    else:
        stream.write('Error type\n')

    stream.write(f'Sum: {matrix_sum(matrix)}\n')
    stream.write(f'\t\tSize: {matrix.size}\n')
    stream.write(f'\t\tOutput type: {matrix.out_type}\n')


def two_dimensional_array_read_from(matrix, stream, size):
    for i in range(size):
        line = stream.readline().rstrip('\n')
        matrix.data.append(list(map(lambda x: int(x), line.split())))

def two_dimensional_array_write_to(matrix, stream, size, out_type):
    if out_type == 1:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write(f'{matrix.data[i][j]} ')
            stream.write('\n\t\t')

    elif out_type == 2:
        for i in range(size):
            for j in range(size):
                stream.write(f'{matrix.data[j][i]} ')
            stream.write('\n\t\t')

    elif out_type == 3:
        for i in range(size):
            for j in range(size):
                stream.write(f'{matrix.data[i][j]} ')
        stream.write('\n\t\t')
    else:
        stream.write('\tError matrix output type\n')


def diagonal_read_from(matrix, stream):
    matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

def diagonal_write_to(matrix, stream, size, out_type):
    if out_type == 1 or out_type == 2:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write('{} '.format(matrix.data[i] if i == j else 0))
            stream.write('\n\t\t')

    elif out_type == 3:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write('{} '.format(matrix.data[i] if i == j else 0))
    else:
        stream.write('\tError matrix output type\n')


def triangle_read_from(matrix, stream):
    matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

def triangle_write_to(matrix, stream, size, out_type):
    if out_type == 1 or out_type == 2:
        stream.write('\t\t')
        index = 0
        for i in range(size):
            for j in range(size):
                if j >= i:
                    stream.write(str(matrix.data[index]) + ' ')
                    index += 1
                else:
                    stream.write('0 ')
            stream.write('\n\t\t')

    elif out_type == 3:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write('{} '.format(matrix.data[i] if i == j else 0))
    else:
        stream.write('\tError matrix output type\n')


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