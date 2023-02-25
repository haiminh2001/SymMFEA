from __future__ import annotations
from typing import Callable, List
import numpy as np
class Node:
    def __init__(self, num_operands: int, func: Callable, is_operand: bool = False):
        self.num_operands:int = num_operands
        self.func: Callable = func
        self.is_operand: bool = is_operand
        
    def add_children(self, children: List[Node]):
        assert len(children) == self.num_operands
        self.children: List[Node] = children
        
    
    def __call__(self, x):
        if self.num_operands < 1:
            return self.func(x)
        elif self.num_operands == 1:
            return self.func(self.children[0](x))
        else:
            return self.func(np.array([child(x) for child in self.children]))