from matrix import matrix_read_from, matrix_write_to, compare, MatrixType, TwoDimArray, Triangle, Diagonal, Matrix


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Container:
    def __init__(self):
        self.start_node = None
        self.size = 0


def container_add(container, data):
    if container.start_node is None:
        container.start_node = Node(data)
    else:
        n = container.start_node
        while n.next is not None:
            n = n.next
        n.next = Node(data)

    container.size += 1


def container_clear(container):
    container.start_node = None
    container.size = 0


def container_read_from(container, stream):
    while line := stream.readline():
        item = matrix_read_from(stream, line)
        container_add(container, item)


def container_write_to(container, stream):
    stream.write(f'Container has {container.size} elements\n')

    if container.start_node != None:
        n = container.start_node
        while n is not None:
            matrix_write_to(n.data, stream)
            n = n.next


def container_sort(container):
    if container.start_node is None:
        print('Empty')
    else:
        n1 = container.start_node
        n2 = container.start_node
        while n1 is not None:
            while n2 is not None:
                if compare(n1.data, n2.data):
                    n1.data, n2.data = n2.data, n1.data
                n2 = n2.next
            n1 = n1.next
            n2 = container.start_node


def container_write_two_dimensional_array_to(container, stream):
    stream.write('Only two dimensional arrays\n')

    n = container.start_node
    while n is not None:
        if n.data.key == MatrixType.two_dimensional_array:
            matrix_write_to(n.data, stream)
        n = n.next


def container_check_matrices(container):
    matrices_1 = []
    n = container.start_node
    while n is not None:
        matrices_1.append(n.data)
        n = n.next

    matrices_2 = matrices_1.copy()

    for matrix_1 in matrices_1:
        for matrix_2 in matrices_2:
            check_matrices(matrix_1, matrix_2)


def check_matrices(matrix_1, matrix_2):
    match matrix_1.obj, matrix_2.obj:
        case TwoDimArray(), TwoDimArray():
            print("Matrices are the same type: TwoDimArray and TwoDimArray")

        case TwoDimArray(), Diagonal():
            print("Matrices are different type: TwoDimArray and Diagonal")

        case TwoDimArray(), Triangle():
            print("Matrices are different type: TwoDimArray and Triangle")

        case Diagonal(), TwoDimArray():
            print("Matrices are different type: Diagonal and TwoDimArray")

        case Diagonal(), Diagonal():
            print("Matrices are the same type: Diagonal and Diagonal")

        case Diagonal(), Triangle():
            print("Matrices are different type: Diagonal and Triangle")

        case Triangle(), TwoDimArray():
            print("Matrices are different type: Triangle and TwoDimArray")

        case Triangle(), Diagonal():
            print("Matrices are different type: Triangle and Diagonal")

        case Triangle(), Triangle():
            print("Matrices are the same type: Triangle and Triangle")

        case _:
            print('Unknown type')
            return

    print(f"First: {matrix_1}, second: {matrix_2}")
    print()