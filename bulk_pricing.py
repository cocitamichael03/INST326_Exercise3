"""Exercise 1 for INST 326, creates a simple game of rock, paper and scissors. 
Driver: Jorge Argueta; jarguet2@umd.edu
Navigator: Michael Vincent Cocita
Assignment: Exercise 1 
Date: 9_9_21
Challenges Encountered:  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
"""


import sys
from argparse import ArgumentParser

def get_cost(number_of_magnets):

    return(float(0) if number_of_magnets < 0 else
    float(.75) if 0 <= number_of_magnets < 50 else
    float(.72) if 99 >= number_of_magnets >= 50 else
    float(.7) if 999 >= number_of_magnets >= 100 else
    float(.67))


def parse_args(args_list):
    
    parser = ArgumentParser()
    parser.add_argument("number_of_magnets", type = int)
    args = parser.parse_args(args_list)
    return args


if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    print(get_cost(arguments.number_of_magnets))
