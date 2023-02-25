
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(os.path.dirname(parent))


from SymMFEA.network import create_function_from_gene
def test_decode():
    
    create_function_from_gene([1, 2, 0, 1, 2])
    assert 1 == 1

test_decode()

