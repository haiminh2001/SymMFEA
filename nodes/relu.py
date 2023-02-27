from .node import Node
import numpy as np
# import numba as nb

# @nb.njit
def relu(operands):
    return operands if operands > 0 else 0

class Relu(Node):
    def __init__(self):
        super().__init__(num_operands = 1, func = relu)
    