from problem import ToyProblem
import argparse
from evolution import MultiObjectiveOptimizer, Optimizer



def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--num_operands", default=100, type=int)
    parser.add_argument("--seed", type=int, default=42)
    parser = Optimizer.add_optimizer_specific_args(parser)
    

    args = parser.parse_args()

    return args

def main():
    args = parse_args()
    problem = ToyProblem(seed = args.seed)
    
    
    optimizer = Optimizer(args)
    population, objs = optimizer.ga(problem)


if __name__ == '__main__':
    main()