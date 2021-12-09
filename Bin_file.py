class Bin(object):
    """Class which represents a bin"""
    def __init__(self):
        """Constructor
        
        Args
        self - instance identifier"""
        self.contents = []
        self.weight = 0

    def __str__(self):
        """Converts a bin object to a string representation
        
        Args
        self - object identifier
        
        Returns
        String representing the object"""
        return str(self.weight) + " : " + str(len(self.contents))

    def __repr__(self):
        """Converts the object for printing
        
        Args
        self - object identifier
        
        Returns
        String representing the object"""
        return str(self.weight) + " : " + str(len(self.contents))

    def __eq__(self, value):
        """Checks if two bins are equal
        
        Args
        self - instance identifier
        value - comparison object identifier
        
        Returns
        True if the objects are the same, false if not"""
        return self.contents == value.contents

    def __lt__(self, value):
        """Checks two bins for less than equality
        
        Args
        self - instance identifier
        value - comparison object identifier
        
        Returns
        True if the objects are the same, false if not"""
        return self.weight < value.weight

    def __gt__(self, value):
        """Checks two bins for greater than equality
        
        Args
        self - instance identifier
        value - comparison object identifier
        
        Returns
        True if the objects are the same, false if not"""
        return self.weight > value.weight

    def add_item(self, item):
        """Adds an item to the bin
        
        Args
        self - instance identifier
        item - item to add"""
        self.contents.append(item)
        self.weight += item




