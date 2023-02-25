
import numpy as np
from . import get_node, Node
from typing import List


def create_function_from_gene(gene: np.ndarray):
    
    
    root = get_node(gene[0,0])()
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
                node_type = gene[0, idx]
                
                #if is operand
                if node_type == 0:
                    node = get_node(node_type)(index = gene[1, idx])
                
                #if is operator
                else:
                    node = get_node(node_type)()
                    stack.append(node)

                children.append(node)
                
            cur_node.add_children(children)
        
        idx += 1
        stack.pop(0)
            
    return root