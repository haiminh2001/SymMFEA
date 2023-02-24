import numpy as np
class Node:
    def __init__(self, num_operands, func) -> None:
        self.num_operands = num_operands
        self.func = func
    
    def __call__(self, operands:np.ndarray):
        return self.func(operands)