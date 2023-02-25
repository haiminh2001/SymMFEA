from .node import Node
import numpy as np
# import numba as nb

# @nb.njit
def add(operands: np.ndarray):
    return np.sum(operands)


class Add(Node):
    def __init__(self):
        super().__init__(num_operands = 2, func = add)
    