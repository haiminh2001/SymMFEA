from .add import Add
from .subtract import Subtract
from .operand import Operand
from .node import Node
from .cos import Cos
from .prod import Prod
NODES = {
    0: Operand,
    1: Add,
    2: Subtract,
    3: Cos,
    4: Prod,
}

def get_node(key:int) -> Node:
    return NODES[key]