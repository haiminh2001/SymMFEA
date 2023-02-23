from sklearn.datasets import make_regression
import argparse
from evolution import MultiObjectiveOptimizer



def parse_args():
    parser = argparse.ArgumentParser()

    parser = MultiObjectiveOptimizer.add_optimizer_specific_args(parser)
    parser.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()

    args.num_terminal = args.num_main + 1
    args.l_main = args.h_main * (args.max_arity - 1) + 1
    args.l_adf = args.h_adf * (args.max_arity - 1) + 1
    args.main_length = args.h_main + args.l_main
    args.adf_length = args.h_adf + args.l_adf
    args.chromosome_length = (
        args.num_main * args.main_length + args.num_adf * args.adf_length
    )
    args.D = args.chromosome_length
    args.mutation_rate = args.adf_length / args.chromosome_length

    return args

def main():
    pass

if __name__ == '__main__':
    X, y = make_regression()
    
    main()