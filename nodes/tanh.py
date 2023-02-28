from .node import Node
import numpy as np
# import numba as nb

# @nb.njit
def tanh(operands):
    return np.tanh(operands)

class Tanh(Node):
    def __init__(self):
        super().__init__(num_operands = 1, func = tanh)
    