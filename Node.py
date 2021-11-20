from Bin_file import Bin
class Node(object):
    def __init__(self, bin_no, item_no):
        self.connections = []
        self.pheromones = []
        self.bin_no = bin_no
        self.item_no = item_no

    def __eq__(self, value):
        return self.bin_no == value.bin_no and self.item_no == value.item_no

    def __str__(self):
        return "Item : " + str(self.item_no)+ "; Bin : " + str(self.bin_no)

    def __repr__(self):
        return str(self)







