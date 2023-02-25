
import sys
import os
import numpy as np
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(os.path.dirname(parent))


from SymMFEA.network import create_function_from_gene
def test_decode():
    #Expression  +, −, cos, ∗, x,−, cos,+, y, x, x, x, x, y, x, y, x
    
    func = create_function_from_gene(np.array([[1, 2, 3, 4, 0, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ,0 ,1 ,0]                           
                                        ]))
    x = np.array([1, 2])
    print(func(x))

test_decode()

