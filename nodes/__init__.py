from .add import Add
from .subtract import Subtract
from .operand import Operand

NODES = {
    0: Operand,
    1: Add,
    2: Subtract,
}