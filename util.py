import random
from .matrix import *

def random_matrix(dim: tuple, rng: tuple) -> "Matrix":
    ls = [random.sample(range(*rng), dim[1]) for _ in range(dim[0])]
    return Matrix(ls)