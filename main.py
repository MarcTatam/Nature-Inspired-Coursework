from random import random
from Bin_file import Bin
from Node import Node

def aco(bins: int, items:[int], ants:int, evaporation_rate:float):
    """Runs the ant colony optimisation algorithm
    
    Args
    bins - an int representing the number of bins
    items - list of integers with each integer representing the weight of the item
    """
    nodes = generate_nodes(bins,len(items))
    paths = []
    fitnesses = []
    for i in range(ants):
        bin_list = []
        for j in range(bins):
            bin_list.append(Bin())
        path = []
        node = nodes[0]
        while node.item_no < len(items):
            total = sum(node.pheromones)
            sumto = 0
            choice = random()
            for j in range(len(node.connections)):
                if choice <= sumto + node.pheromones[j]/total and sumto <= choice:
                    node = node.connections[j]
                    path.append(node.bin_no)
                    print(path)
                    bin_list[node.bin_no-1].add_item(items[node.item_no-1])
                    break
                else:
                    sumto += node.pheromones[j]/total
        node = nodes[0]
        fitness = max(bin_list).weight-min(bin_list).weight
        fitnesses.append(100/fitness)
        paths.append(path)
        for route in path:
            node.pheromones[route - 1] += 100/fitness
        for node in nodes:
            for route_ind in range(len(node.pheromones)):
                node.pheromones[route_ind] *= evaporation_rate

    
def generate_nodes(bins: int, items: int):
    nodes = []
    start_node = Node(0,0)
    nodes.append(start_node)
    previous_level = [start_node]
    for i in range(items):
        item_no = i + 1
        this_level = []
        for j in range(bins):
            bin_no = j +1
            temp_node = Node(bin_no,item_no)
            this_level.append(temp_node)
            for node in previous_level:
                node.connections.append(temp_node)
                node.pheromones.append(random())
        nodes = nodes + this_level
        previous_level = this_level
    end_node = Node(0,items+1)
    for node in previous_level:
        node.connections.append(end_node)
        node.pheromones.append(1)
    nodes.append(end_node)
    return nodes


if __name__ == "__main__":
    print(aco(3,[4,5,6,7,8,9,2,3,4,5],10,0.9))