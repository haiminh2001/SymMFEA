
import numpy as np
from . import get_node, Node
from typing import List


def create_function_from_gene(gene: np.ndarray):
    
    
    root = get_node(gene[0])()
    stack: List[Node] = [root]
    idx = 1
    #get head
    while len(stack):
        cur_node = stack[0]
        
        if cur_node.is_operand:
            pass
        
        else:
            children = []
            num_children = cur_node.num_operands
            for _ in range(num_children):
                node = get_node(gene[idx])()
                stack.append(node)
                children.append(node)
                
            cur_node.add_children(children)
        
        print(len(stack))
        stack.pop(0)
            
    return root