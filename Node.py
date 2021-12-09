from Bin_file import Bin
class Node(object):
    """Class for node obejcts"""
    def __init__(self, bin_no, item_no):
        """Constructor
        
        Args
        self - instance identifier
        bin_no - integer which represents which bin node sits at
        item_no - integer which represents which item index this node sits at"""
        self.connections = []
        self.pheromones = []
        self.bin_no = bin_no
        self.item_no = item_no

    def __eq__(self, value):
        """Checks if two nodes are equal
        
        Args
        self - instance identifier
        value - comparison object identifier
        
        Returns
        True if the objects are the same, false if not"""
        return self.bin_no == value.bin_no and self.item_no == value.item_no

    def __str__(self):
        """Converts a node object to a string representation
        
        Args
        self - object identifier
        
        Returns
        String representing the object"""
        return "Item : " + str(self.item_no)+ "; Bin : " + str(self.bin_no)

    def __repr__(self):
        """Converts the object for printing
        
        Args
        self - object identifier
        
        Returns
        String representing the object"""
        return str(self)







