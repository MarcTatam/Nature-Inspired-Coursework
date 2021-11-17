from Bin_file import Bin
from Node import Node

def aco(bins: int, items:[int], ants:int):
    """Runs the ant colony optimisation algorithm
    
    Args
    bins - an int representing the number of bins
    items - list of integers with each integer representing the weight of the item
    """
    bin_list = []
    for i in range(bins):
        bin_list.append(Bin())
    


if __name__ == "__main__":
    aco(5,[6,7,8,9],2)
