from .add import Add
from .subtract import Subtract
from .operand import Operand
from .node import Node
from .cos import Cos
from .prod import Prod
from .relu import Relu
NODES = {
    0: Operand,
    1: Add,
    2: Subtract,
    3: Cos,
    4: Prod,
    # 5: Relu,
}
def get_node(key:int) -> Node:
    return NODES[key]

from .setup_model import create_function_from_gene



