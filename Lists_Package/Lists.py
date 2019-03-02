from Lists_Package.Nodes import SingleNode, DoubleNode
import unittest as ut

"""
Define Different List Types
"""


class SinglyLinkedList(object):

    def __init__(self, *args, **kwargs):

        self.__size = 0     # N-elements
        self.__head = None  # Head of the list

        self.__cur = None   # Pointer

    def __str__(self):
        pass

    def __iter__(self):
        self.__cur = self.get_head()
        return self

    def __next__(self):
        if self.__cur is None:
            raise StopIteration()

        result = self.__cur.get_item()

        self.__cur = self.__cur.get_next()

        return result

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __len__(self):
        pass

    def __eq__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def get_head(self):
        return self.__head

    def set_head(self, item):
        self.__head = SingleNode(item)

    def insert(self, item, idx=0):
        if idx >= self.size() and self.size() != 0:
            raise IndexError("Index is out of range")

        if self.size() == 0:
            self.set_head(item=item)
            self.__size += 1

        elif self.size() != 0 and idx != 0:
            self.__cur = self.get_head()
            for i in range(idx-1):
                self.__cur = self.__cur.get_next()

            old_next = self.__cur.get_next()
            self.__cur.set_next(SingleNode(item=item))
            self.__cur.get_next().set_next(old_next)

            self.__size += 1

        elif self.size() != 0 and idx == 0:
            old_head = self.get_head()
            self.set_head(item=item)
            self.get_head().set_next(old_head)

            self.__size += 1

    def size(self):
        return self.__size

    def delete(self, item):
        pass

    def pop(self, idx):
        pass


class DoublyLinkedList(object):

    def __init__(self, *args, **kwargs):

        self.__size = 0
        self.__head = None
        self.__tail = None

    def __str__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __len__(self):
        pass

    def __eq__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def get_head(self):
        pass

    def set_head(self, item):
        pass

    def get_tail(self):
        pass

    def set_tail(self):
        pass

    def insert(self, item):
        pass

    def size(self):
        pass

    def delete(self, item):
        pass

    def pop(self, idx):
        pass


if __name__ == "__main__":

    class ListTestCases(ut.TestCase):

        def setUp(self):

            self.SLL = SinglyLinkedList()
            self.DLL = DoublyLinkedList()

    def run_TestCases():
        suite = ut.TestLoader().loadTestsFromTestCase(ListTestCases)
        ut.TextTestRunner(verbosity=2).run(suite)

    run_TestCases()
