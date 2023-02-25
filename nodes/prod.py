

from .node import Node
import numpy as np
# import numba as nb

# @nb.njit
def prod(operands: np.ndarray):
    return operands[0] * operands[1]


class Prod(Node):
    def __init__(self):
        super().__init__(num_operands = 2, func = prod)
        
    