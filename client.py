import sys

from container import (
    container_read_from,
    container_write_to,
    container_clear,
    container_sort,
    container_write_two_dimensional_array_to,
    Container
)


def main():
    try:
        input_file = open(sys.argv[1], "r")
    except OSError:
        print('Opening file error')
        sys.exit(1)

    print('Start')

    cont = Container()
    container_read_from(cont, input_file)

    print('Filled container')

    #container_sort(cont)
    try:
        output_file = open(sys.argv[2], "w")
    except OSError:
        print('Opening file error')
        sys.exit(1)
    finally:
        input_file.close()
    container_write_to(cont, output_file)
    #container_write_two_dimensional_array_to(cont, output_file)

    container_clear(cont)

    print('Empty container')
    container_write_to(cont, output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()