from unittest import TestCase
from Lists_Package.Lists import SinglyLinkedList
from Lists_Package.Nodes import SingleNode

class TestSinglyLinkedList(TestCase):

    def setUp(self):

        self.SLL = SinglyLinkedList()

    def test_get_head(self):

        self.assertEqual(None, self.SLL.get_head())
        self.SLL.insert(1)
        self.assertEqual(SingleNode(1), self.SLL.get_head())

    def test_set_head(self):
        self.fail()

    def test_insert(self):
        self.fail()

    def test_size(self):
        self.fail()

    def test_is_empty(self):

        self.assertEqual(self.SLL.is_empty(), True)

    def test_delete(self):
        self.fail()

    def test_pop(self):
        self.fail()

    def test_sort(self):
        self.fail()

    def test_reverse(self):
        self.fail()
