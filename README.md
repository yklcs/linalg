# linalg

[![PyPI version](https://badge.fury.io/py/linalg.svg)](https://badge.fury.io/py/linalg)


## What is this?

NOT intended to be the best or fastest.

NOT intended to be production-grade (yet).

IS intended to be fully vanilla python3.

IS meant as an educational tool.

## Usage

This package provides the `Matrix` class and utility functions.

    import linalg
    from linalg import *  # import the Matrix class and utility functions top-level
    from linalg import Matrix  # import the Matrix class

To create a matrix object, initialize it with a 2D list or use `Matrix.zeroes()` or `Matrix.identity()`. You can also use `random_matrix()`.

    mat = Matrix([[3, 4, 5], [2, 5, -1], [0, 2, 1]])  # 3x3 matrix
    mat = Matrix.zeroes(4, 2)  # 4x2 zero matrix
    mat = Matrix.identity(4, 4)  # 4x4 identity matrix
    mat = random_matrix((2, 3), (-10, 10))  # 2x3 matrix with elements within (-10, 10)

After that, you can use multiple functions within the `Matrix` class to perform linear algebraic operations.

## Todo

- [] Properly implement `random_matrix()`
- [] Add other linear algebraic operations
- [] Implement vectors
- [] Add documentation
