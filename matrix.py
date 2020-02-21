import copy


def check_type(x, y=0):
    if y == 0:
        y = [[]]

    if not (type(x) is list and type(y) is list):
        if not (type(x[0]) is list and type(y[0]) is list):
            raise RuntimeError("x{0}must be of type: list of list --> [[]]".format(
                " " if y == [[]] else " and y "
            ))  # TODO: correct text


def is_row_matrix(x):
    return len(x) == 1 or len(x[0]) == 1


def is_dim_equal(x, y):
    return (len(x) == len(y)) and (len(x[0]) == len(y[0]))


def zero_matrix(m, n):
    t = []
    for i in range(m):
        t.append([])
        for j in range(n):
            t[i].append(0)

    return t


def dot(x, y):
    check_type(x, y)

    m_x = len(x)
    n_x = len(x[0])

    m_y = len(y)
    n_y = len(y[0])

    if n_x != m_y:
        raise RuntimeError('X cols must be equal to Y rows')

    # print("(", m_x, ",", n_x, ")", ", ", "(", m_y, ",", n_y, ")")

    result = []
    for i in range(m_x):
        r1 = []
        for j in range(n_y):
            sum1 = 0
            for k in range(n_x):
                sum1 += x[i][k] * y[k][j]
            r1.append(sum1)
        result.append(r1)

    return result


def dot_scalar(x, n):
    check_type(x)

    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] *= n

    return x


def diff(x, y):
    check_type(x, y)
    if is_row_matrix(x) and is_row_matrix(y):
        if is_dim_equal(x, y):
            t = zero_matrix(1, len(x[0]))
            for i in range(len(x[0])):
                t[0][i] = x[0][i] - y[0][i]
        else:
            raise RuntimeError("Both matrices must have the same dimension")
    else:
        raise RuntimeError("Arguments must be matrices of dimension 1xN")

    return t


def diff_scalar(x, n):
    if is_row_matrix(x):
        for i in range(len(x[0])):
            x[0][i] -= n
    else:
        raise RuntimeError("Arguments must be matrices of dimension 1xN")

    return x


def transpose(x):
    check_type(x)

    m = len(x)
    n = len(x[0])
    t = zero_matrix(n, m)
    for i in range(n):
        for j in range(m):
            t[i][j] = x[j][i]

    return t


def offset_x(x):
    check_type(x)

    for i in range(len(x)):
        x[i].insert(0, 1)

    return x


# print(dot([[1, 2], [1, 2]], [[1, 2, 3], [2, 3, 4]]))
# print(transpose([[1, 2, 3], [4, 4, 5]]))
# print(offset_x([[1, 2], [2, 3]]))
# print(diff([[1, 5]], [[2, 4]]))
# print(dot_scalar([[1, 2], [3, 4]], 5))
# print(diff_scalar([[1, 2, 3, 4]], 5))
