import matplotlib.pyplot as plt
import numpy as np
import main as aco
def bpp1():
    """Graphs the BPP1 absolute values"""
    means = [1633,1473,760,1235]
    min_error = [294,159,185,317]
    max_error = [232,150,76,575]
    x = ["Experiment 1","Experiment 2","Experiment 3","Experiment 4"]
    fig, ax = plt.subplots()
    width = 0.8
    ax.bar(x, means, width=width, color='b', yerr = [min_error,max_error],error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2))
    ax.set_ylabel("Fitness")
    ax.set_title("BPP1")
    plt.show()

def bpp2():
    """Graphs the BPP2 absolute values"""
    means = [902382,857216,809426,985268]
    min_error = [54671,67247,134759,117938]
    max_error = [31619,62865,62145,77083]
    x = ["Experiment 1","Experiment 2","Experiment 3","Experiment 4"]
    fig, ax = plt.subplots()
    width = 0.8
    ax.bar(x, means, width=width, color='b', yerr = [min_error,max_error],error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2))
    ax.set_ylabel("Fitness")
    ax.set_title("BPP2")
    plt.show()

def bpp1_er():
    items = []
    xs = []
    ys = []
    for i in range(1,150):
        items.append(i)
    for i in range(50, 1,-1):
        print(i)
        er = i/51
        xs.append(er)
        ys.append(min(aco.aco(10,items,10,er)[1]))
    fig, ax = plt.subplots()
    width = 0.8
    ax.scatter(xs, ys)
    ax.set_ylabel("Fitness")
    ax.set_xlabel("Evaporation Rate")
    ax.set_title("BPP1")
    plt.show()

def bpp1_er():
    items = []
    xs = []
    ys = []
    for i in range(1,150):
        items.append(i**2)
    for i in range(50, 1,-1):
        print(i)
        er = i/51
        xs.append(er)
        ys.append(min(aco.aco(50,items,10,er)[1]))
    fig, ax = plt.subplots()
    width = 0.8
    ax.scatter(xs, ys)
    ax.set_ylabel("Fitness")
    ax.set_xlabel("Evaporation Rate")
    ax.set_title("BPP2")
    plt.show()


if __name__ == "__main__":
    bpp1_er()
