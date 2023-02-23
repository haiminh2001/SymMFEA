from sklearn.datasets import make_regression
from evolution import create_function_from_gene
class Problem:
    def __init__(self, eval_func) -> None:
        self.X, self.y = make_regression() 
        self.eval_func = eval_func 
        
    
    def evaluate(self, gene):
        function = create_function_from_gene(gene) 
        
        y_hat = function(self.X)
        
        return self.eval_func(self.y, y_hat)