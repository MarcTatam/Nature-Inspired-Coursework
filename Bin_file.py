class Bin(object):
    def __init__(self):
        self.contents = []
        self.weight = 0

    def __str__(self):
        return str(self.weight) + " : " + str(len(self.contents))

    def __repr__(self):
        return str(self.weight) + " : " + str(len(self.contents))

    def __eq__(self, value):
        return self.contents == value.contents

    def __lt__(self, value):
        return self.weight < value.weight

    def __gt__(self, value):
        return self.weight > value.weight

    def add_item(self, item):
        self.contents.append(item)
        self.weight += item




