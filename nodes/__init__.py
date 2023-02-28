from .add import Add
from .subtract import Subtract
from .operand import Operand
from .node import Node
from .tanh import Tanh
from .prod import Prod
from .exp import Exp
from .relu import Relu
NODES = {
    0: Operand,
    1: Add,
    2: Subtract,
    3: Tanh,
    4: Prod,
    5: Exp,
    # 5: Relu,
}
MAX_OPERANDS = 3
def get_node(key:int) -> Node:
    return NODES[key]

from .setup_model import create_function_from_gene



