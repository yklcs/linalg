"""Main functions and classes"""

from linalg import Matrix
from linalg.create import *
from linalg.decompose import *
from linalg.solve import *
from linalg.unary import *
from linalg.data import *

__all__ = ["Matrix"]
__all__.extend(create.__all__)
__all__.extend(decompose.__all__)
__all__.extend(solve.__all__)
__all__.extend(unary.__all__)
__all__.extend(data.__all__)
