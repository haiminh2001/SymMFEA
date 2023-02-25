from .node import Node
import numpy as np
# import numba as nb

# @nb.njit
def cos(operands):
    return np.cos(operands)

class Cos(Node):
    def __init__(self):
        super().__init__(num_operands = 1, func = cos)
    