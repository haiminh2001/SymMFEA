from argparse import ArgumentParser
import numpy as np
from .operator import Operator, MultiObjectiveOperator
from nodes import NODES
from problem import Problem
from tqdm.auto import tqdm

class Optimizer:
    def __init__(self, args):
        self.head_length: int = args.num_operators
        self.tail_length: int = args.num_operands
        self.D: int = self.head_length + self.tail_length
        self.N: int = args.popsize
        self.T: int = args.num_iter
        self.operator = Operator(None, None)

    def ga(self, problem: Problem, return_best=True):
        #lb, ub is 2 list with same length as chromosome (D), indicating value range of each node 
        
        
        ub = np.stack(( 
                      np.full(self.D, len(NODES) - 1),
                      np.full(self.D, problem.num_decision_variables - 1),
                      np.full(self.D, 100), 
                      np.full(self.D, 100), 
                      ))
        
        
        #tail must contain only operands
        ub[0, self.head_length : self.D] = 1
        
        lb = np.concatenate((np.zeros((2, self.D)),
                       np.full((2,self.D), -100)
                       ))
        #root must be operator
        lb[0, 0] = 1
        
        self.operator.lb = lb
        self.operator.ub = ub
        

        # if not os.path.exists(self.save_dict_path):
            # initialization
           
        population = np.random.randint(low=lb, high=ub, size=(self.N, 4, self.D))
        # first evaluation
        
        fitness = [problem.evaluate(population[i, :, :]) for i in range(self.N)]
        start_generation = 1

        with tqdm(range(start_generation, self.T)) as pbar: 
            for t in pbar:
                
                # reproduction
                offspring = self.operator.uniform_crossover(population)
                offspring = self.operator.mutate(offspring)

                # evaluation on offspring
                offspring_fitness = [
                    problem.evaluate(offspring[i, :], is_print = t > 25) for i in range(self.N)
                ]
                pbar.set_description(f"GENERATION: {t} / {self.T} -- {np.max(fitness)}")
                

                # selection
                population, fitness = self.operator.select(
                    population, fitness, offspring, offspring_fitness
                )
                    

                # # save checkpoint
                # Optimizer.save_checkpoint(t, population, fitness, self.save_dict_path)

        # output
        if return_best:
            return self.best_population(population, fitness)
        else:
            return population, fitness

    def best_population(self, population, fitness):
        return population[0], fitness[0]

    @staticmethod
    def add_optimizer_specific_args(parent_parser):
        parser = ArgumentParser(parents=[parent_parser], add_help=False)
        parser.add_argument("--popsize", default=100, type=int)
        parser.add_argument("--num_iter", default=100, type=int)
        return parser


class MultiObjectiveOptimizer(Optimizer):
    def __init__(self, args):
        super().__init__(args)
        self.operator = MultiObjectiveOperator(None, None)

    def best_population(self, population, fitness):
        return self.operator.best_front(population, fitness)
