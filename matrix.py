import sys
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
    try:
        k = int(line)
    except Exception:
        print('Reading type of matrix error')
        stream.close()
        sys.exit(1)

    matrix = Matrix()
    try:
        matrix.size = int(stream.readline().rstrip('\n'))
    except Exception:
        print('Reading size error')
        stream.close()
        sys.exit(1)
    try:
        matrix.out_type = int(stream.readline().rstrip('\n'))
    except Exception:
        print('Reading out type error')
        stream.close()
        sys.exit(1)

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
    try:
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
            sys.exit(1)
    except Exception:
        print('Writing matrix type to file error')
        stream.close()
        sys.exit(1)

    try:
        stream.write(f'Sum: {matrix_sum(matrix.obj)}\n')
        stream.write(f'\t\tSize: {matrix.size}\n')
        stream.write(f'\t\tOutput type: {matrix.out_type}\n')
    except Exception:
        print('Writing matrix properties to file error')
        stream.close()
        sys.exit(1)


def two_dimensional_array_read_from(matrix, stream, size):
    try:
        for i in range(size):
            line = stream.readline().rstrip('\n')
            matrix.data.append(list(map(lambda x: int(x), line.split())))
    except:
        print('Reading two-dimensional array from file error')
        stream.close()
        sys.exit(1)

def two_dimensional_array_write_to(matrix, stream, size, out_type):
    try:
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
    except:
        print('Writing two-dimensional array to file error')
        stream.close()
        sys.exit(1)


def diagonal_read_from(matrix, stream):
    try:
        matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))
    except:
        print('Reading diagonal matrix from file error')
        stream.close()
        sys.exit(1)

def diagonal_write_to(matrix, stream, size, out_type):
    try:
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
    except:
        print('Writing diagonal matrix to file error')
        stream.close()
        sys.exit(1)


def triangle_read_from(matrix, stream):
    try:
        matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))
    except:
        print('Reading triangle matrix from file error')
        stream.close()
        sys.exit(1)

def triangle_write_to(matrix, stream, size, out_type):
    try:
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
    except:
        print('Writing triangle matrix to file error')
        stream.close()
        sys.exit(1)


def compare(first, second):
    return matrix_sum(first) < matrix_sum(second)


def matrix_sum(matrix):
    try:
        s = 0
        for item in matrix.data:
            if isinstance(item, int):
                s += item
            else:
                s += sum(item)
        return s
    except Exception:
        print('Sum calculation error')