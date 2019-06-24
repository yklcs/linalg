"""Main functions and classes"""

__all__ = ["Matrix"]

from .matrix import Matrix
from .create import *
from .decompose import *
from .solve import *
from .unary import *
from .data import *

__all__.extend(create.__all__)
__all__.extend(decompose.__all__)
__all__.extend(solve.__all__)
__all__.extend(unary.__all__)
__all__.extend(data.__all__)
