from random import random
import matplotlib.pyplot as plt
from Bin_file import Bin
from Node import Node

def aco(bins: int, items:[int], ants:int, evaporation_rate:float):
    """Runs the ant colony optimisation algorithm
    
    Args
    bins - an int representing the number of bins
    items - list of integers with each integer representing the weight of the item
    """
    epochs = int(10000/ants)
    nodes = generate_nodes(bins,len(items))
    paths = []
    fitnesses = []
    actual_fitnesses = []
    for epoch in range(epochs):
        print(epoch)
        epoch_paths = []
        epoch_fitnesses = []
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
                        bin_list[node.bin_no-1].add_item(items[node.item_no-1])
                        break
                    else:
                        sumto += node.pheromones[j]/total
            fitness = max(bin_list).weight-min(bin_list).weight
            actual_fitnesses.append(fitness)
            epoch_fitnesses.append(100/fitness)
            epoch_paths.append(path)
        for path_ind in range(len(epoch_paths)):
            node = nodes[0]
            path = epoch_paths[path_ind]
            fitness = epoch_fitnesses[path_ind]
            for route in path:
                node.pheromones[route - 1] += fitness
                node = node.connections[route - 1]
        for node in nodes:
            for route_ind in range(len(node.pheromones)):
                node.pheromones[route_ind] *= evaporation_rate
        fitnesses = fitnesses + epoch_fitnesses
        paths = paths + epoch_paths
    return fitnesses, actual_fitnesses

    
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
    items = []
    xs = []
    fitness_chart = []
    for j in range(1, 501):
        items.append(j**2)
    x = []
    fitnesses, actual_fitnesses = aco(50,items,10,0.9)
    print(min(actual_fitnesses))
    #for i in range(len(fitnesses)):
        #x.append(i)
    #xs.append(x)
    #fitness_chart.append(actual_fitnesses)
    #fig, ax = plt.subplots()
    #plt1 = ax.plot(xs[0], fitness_chart[0], c = "red")
    #plt2 = ax.plot(xs[1], fitness_chart[1], c = "orange")
    #plt3 = ax.plot(xs[2], fitness_chart[2], c = "darkolivegreen")
    #plt4 = ax.plot(xs[3], fitness_chart[3], c = "cyan")
    #plt5 = ax.plot(xs[4], fitness_chart[4], c = "fuchsia")
    #ax.set_xlabel('Path Number', fontsize=15)
    #ax.set_ylabel('Fitness', fontsize=15)
    #ax.legend([plt1, plt2, plt3, plt4, plt5], ["Run 1", "Run 2","Run 3","Run 4","Run 5"])
    #plt.show()

    #x= []
    #for i in range(len(fitnesses)):
    #    x.append(i)
    #fig, ax = plt.subplots()
    #ax.plot(x,fitnesses)
