from linalg.matrix import Matrix
import random


def zeroes(i: int, j: int) -> "Matrix":
    """creates an i by j zero matrix
    
    :param i: number of columns
    :type i: int
    :param j: number of rows
    :type j: int
    :return: an i by j matrix filled with zeroes
    :rtype: Matrix
    """
    return Matrix([[0] * j for _ in range(i)], valid=True)


def identity(n: int) -> "Matrix":
    """generates an n by n identity matrix
    
    :param n: number of rows/columns
    :type n: int
    :return: n by b indentity matrix
    :rtype: Matrix
    """
    id = [[int(i == j) for j in range(n)] for i in range(n)]
    return Matrix(id)


def random_matrix(dim: tuple, rng: tuple) -> "Matrix":
    """generates a random matrix
    
    :return: randomized matrix of specified size and range
    :rtype: Matrix
    """
    ls = [random.sample(range(*rng), dim[1]) for _ in range(dim[0])]
    return Matrix(ls)
