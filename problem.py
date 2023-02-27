from sklearn.datasets import make_regression
from sklearn.metrics import mean_absolute_percentage_error as MAPE
from nodes import create_function_from_gene
from argparse import ArgumentParser
from typing import Callable
import numpy as np
class Problem:
    def __init__(self, X, y, eval_func: Callable = MAPE):
        self.X, self.y = X, y
        self.eval_func = eval_func 
        
        
    @staticmethod
    def add_optimizer_specific_args(parent_parser):
        parser = ArgumentParser(parents=[parent_parser], add_help=False)
        parser.add_argument("--popsize", default=100, type=int)
        parser.add_argument("--num_iter", default=100, type=int)
        return parser
    
    @property
    def num_decision_variables(self):
        return self.X.shape[1]
    

    def evaluate(self, gene):
        function = create_function_from_gene(gene) 
        
        
        y_hat = np.array([function(x) for x in self.X])
        
        return -self.eval_func(self.y, y_hat)
    
    
class ToyProblem(Problem):
    def __init__(self, eval_func: Callable = MAPE):
        X, y = make_regression()
        super().__init__(X, y, eval_func)
        
    