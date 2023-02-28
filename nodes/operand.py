from .node import Node
import numpy as np

class Operand(Node):
    def __init__(self, index: int, weight:float = 1, bias:float = 0):
        def transform(x):
            return x[index] * np.log(np.abs(weight) + 1) * np.sign(weight) + bias        
        
        super().__init__(num_operands = 0, func = transform, is_operand= True)