class Bin(object):
    def __init__(self):
        self.contents = []
        self.weight = 0

    def __str__(self):
        return str(self.weight) + " : " + str(self.contents)

    def __repr__(self):
        return str(self.weight) + " : " + str(self.contents)

    def add_item(self, item):
        self.contents.append(item)
        self.weight += item




