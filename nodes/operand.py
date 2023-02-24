from .node import Node


class Operand(Node):
    def __init__(self, value):
        def identical():
            return value        
        super().__init__(num_operands = 1, func = identical)