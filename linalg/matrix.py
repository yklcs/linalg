from operator import *
import linalg

class MatrixError(Exception):
    pass


class Matrix:
    """Implements Matrices.
    """

    def __init__(self, mat, valid=False):
        if not valid:
            try:
                self._is_valid(mat)
            except Exception as e:
                raise e

        self.shape = (len(mat), len(mat[0]))
        self.matrix = mat

    def _is_valid(self, mat):
        """checks if given matrix is valid

        :param mat: Matrix to test
        :type mat: Matrix
        :raises MatrixError: raises MatrixError
        """
        matlen = len(mat[0])
        for row in mat:
            if len(row) != matlen:
                raise MatrixError("Malformed matrix")
            for i in row:
                assert isinstance(i, (int, float, complex))

    def _is_square(self) -> bool:
        return self.shape[0] == self.shape[1]

    def _pivotize(self) -> ("Matrix", int):
        """creates the pivoting matrix for self

        :return: the pivoting matrix for self and the number of permutations
        :rtype: Matrix, int
        """
        assert self._is_square()
        n = self.shape[0]
        S = 0
        a = self.identity(n)
        for j in range(n):
            row = max(range(j, n), key=lambda i: abs(self[i][j]))
            if j != row:
                S += 1
                a[j], a[row] = a[row], a[j]

        return a, S

    @staticmethod
    def inverse(mat: "Matrix") -> "Matrix":
        """returns the inverse matrix of mat
        
        :param mat: the matrix to invert
        :type mat: Matrix
        :return: the inverse matrix of mat
        :rtype: Matrix
        """
        assert mat._is_square()
        return linalg.solve.solve(mat, linalg.create.identity(mat.shape[0]))

    @staticmethod
    def transpose(mat: "Matrix") -> "Matrix":
        x, y = mat.shape
        return Matrix([[mat[a][b] for a in range(y)] for b in range(x)])

    @staticmethod
    def as_list(cls, mat: "Matrix") -> list:
        """returns the matrix as a list
        
        :param mat: matrix to convert
        :type mat: Matrix
        :return: matrix as a 2d list
        :rtype: list
        """
        return mat.matrix

    @staticmethod
    def det(cls, mat: "Matrix") -> float:
        """computes the determinant for a given matrix
        
        :param mat: matrix to compute the determinant for
        :type mat: Matrix
        :return: the determinant for mat
        :rtype: float
        """
        assert mat._is_square()

        L, U, P, S = linalg.decompose.lu(mat)
        n = mat.shape[0]
        l_pd, u_pd = 1, 1
        for i in range(n):
            l_pd *= L[i][i]
            u_pd *= U[i][i]
        return (-1) ** S * l_pd * u_pd

    def __str__(self):
        r = ""
        for i in range(self.shape[0]):
            r += "|"
            for j in range(self.shape[1]):
                r += "{:^6.5}".format(str(self[i][j]))
            r += "|"
            r += "\n"

        return r

    def __add__(self, x):
        return Matrix(
            list([list(map(add, self[i], x[i])) for i in range(self.shape[0])]),
            valid=True,
        )

    def __neg__(self):
        return Matrix(
            list([list(map(neg, self[i])) for i in range(self.shape[0])]), valid=True
        )

    def __sub__(self, x):
        return self.__add__(-x)

    def __matmul__(self, x: "Matrix"):
        result = Matrix(
            [
                [sum(a * b for a, b in zip(self_row, x_col)) for x_col in zip(*x)]
                for self_row in self
            ]
        )

        return result

    def __mul__(self, x: float):
        return Matrix([[a * x for a in row] for row in self])

    def __rmul__(self, x: float):
        return self.__mul__(x)

    def __getitem__(self, i):
        return self.matrix[i]

    def __setitem__(self, key, item):
        self.matrix[key] = item
