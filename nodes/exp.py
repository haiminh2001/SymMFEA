from .node import Node
import numpy as np
# import numba as nb

# @nb.njit
def exp(operands):
    return np.exp(operands)

class Exp(Node):
    def __init__(self):
        super().__init__(num_operands = 1, func = exp)
    