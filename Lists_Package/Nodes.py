import unittest as ut

"""
Define List Nodes Here
"""


class Node(object):

    def __init__(self, item=None):

        self.__item = item

    def get_item(self):
        return self.__item

    def set_item(self, item):
        self.__item = item


class SingleNode(Node):

    def __init__(self, item):

        super().__init__(item=item)

        self.__next = None

    def __eq__(self, other):
        if type(other) != SingleNode:
            return False

        if type(other) == SingleNode:
            if self.get_item() == other.get_item():
                return True
            else:
                return False

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node


class DoubleNode(Node):

    def __init__(self, item):

        super().__init__(item=item)

        self.__next = None
        self.__prev = None

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def get_prev(self):
        return self.__prev

    def set_prev(self, node):
        self.__prev = node


if __name__ == "__main__":

    pass
