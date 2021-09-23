
import sys
from argparse import ArgumentParser

def get_cost(number_of_magnets):

    return(float(0) if number_of_magnets < 0 else
    float(.75) if 0 <= number_of_magnets < 50 else
    float(.72) if 99 >= number_of_magnets >= 50 else
    float(.7) if 999 >= number_of_magnets >= 100 else
    float(.67))*number_of_magnets


if __name__ == "__main__":
    print(get_cost(1000))
