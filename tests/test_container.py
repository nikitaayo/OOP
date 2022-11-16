from container import (
    container_add,
    container_read_from,
    container_write_to,
    container_clear,
    container_sort,
    Container
)


def test_clear():
    container = Container()
    for i in range(10):
        container_add(container, i)

    container_clear(container)

    assert len(container.data) == 0


def test_push_back():
    container = Container()
    container_add(container, '123')
    container_add(container, (1, 2, 3))
    container_add(container, [1, 2, 3])

    array = [item for item in container.data]

    assert ['123', (1, 2, 3), [1, 2, 3]] == array


def test_len():
    container = Container()
    for i in range(10):
        container_add(container, i)

    assert len(container.data) == 10


def test_read_from():
    container = Container()

    with open('tests/input.txt', 'r') as file:
        container_read_from(container, file)

    assert len(container.data) != 0


def test_write_to():
    container = Container()

    with open('tests/input.txt', 'r') as file:
        container_read_from(container, file)

    with open('tests/output.txt', 'w') as file:
        container_write_to(container, file)

    file_obs = open("tests/output.txt", "r")
    file_exp = open("tests/output_test_write.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_sort():
    container = Container()

    with open('tests/input.txt', 'r') as file:
        container_read_from(container, file)

    container_sort(container)
    with open("tests/output_test_sort.txt", "w") as file:
        container_write_to(container, file)

    file_obs = open("tests/output_sort.txt", "r")
    file_exp = open("tests/output_test_sort.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_write_two_dim_array_to():
    container = Container()

    with open('tests/input.txt', 'r') as file:
        container_read_from(container, file)

    with open("tests/output_test_write_two_dim_array_to.txt", "w") as file:
        container_write_to(container, file)

    file_obs = open("tests/output_write_two_dim_array.txt", "r")
    file_exp = open("tests/output_test_write_two_dim_array_to.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()
