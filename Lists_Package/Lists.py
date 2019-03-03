from Lists_Package.Nodes import SingleNode, DoubleNode

import numpy as np
from collections import Iterable

import unittest as ut
"""
Define Different List Types
"""


class SinglyLinkedList(object):

    def __init__(self, iterable=None, *args, **kwargs):

        self.__size = 0     # N-elements
        self.__head = None  # Head of the list

        self.__cur = None   # Pointer

        if iterable is None:
            pass

        else:
            if isinstance(iterable, Iterable):
                for item in reversed(iterable):
                    self.insert(item)
            else:
                raise TypeError("Object is not iterable")

    def __str__(self):
        string = "SLL:[ "
        for item in self:
            string += f"{item}, "

        if self.size() != 0:
            string = string[:-2]

        else:
            string = string[:-1]

        string += " ]"
        return string

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
        self.__cur = self.__head

        if type(key) != slice:

            for idx in range(self.size()):
                if idx == key:
                    return self.__cur.get_item()

                else:
                    self.__cur = self.__cur.get_next()

        elif type(key) == slice:

            newlist = SinglyLinkedList()

            start, stop, step = key.start, key.stop, key.step

            if start is None:
                start = 0

            if step is None:
                step = 1

            if stop is None:
                stop = self.size()

            for idx in range(self.size()):
                if idx in range(start, stop, step):
                    newlist.insert(self.__cur.get_item())
                    self.__cur = self.__cur.get_next()
                else:
                    self.__cur = self.__cur.get_next()

            return newlist

    def __setitem__(self, key, value):
        self.__cur = self.__head

        for idx in range(self.size()):
            if idx == key:
                self.__cur.set_item(value)
                return
            else:
                self.__cur = self.__cur.get_next()

    def __len__(self):
        return self.size()

    def __reversed__(self):

        prev = None
        cur = self.get_head()
        nxt = None

        while cur is not None:

            nxt = cur.get_next()
            cur.set_next(prev)
            prev = cur
            cur = nxt
        self.__head = prev
        return self

    def __eq__(self, other):

        for node_i, node_j in zip(self, other):
            if node_i == node_j:
                continue
            else:
                return False

        return True

    def __abs__(self):

        for idx, item in enumerate(self):
            self[idx] = abs(item)

        return self

    def __pow__(self, power, modulo=None):

        for idx, item in enumerate(self):
            self[idx] = item**power

        if modulo is not None:
            for idx, item in enumerate(self):
                self[idx] = item % modulo

        return self

    def __add__(self, other):

        if isinstance(other, Iterable):
            for idx in range(len(other[:self.size()])):
                self[idx] += other[idx]

        else:
            for idx in range(len(self)):
                self[idx] += other

    def __sub__(self, other):

        if isinstance(other, Iterable):
            for idx in range(len(other[:self.size()])):
                self[idx] -= other[idx]

        else:
            for idx in range(len(self)):
                self[idx] -= other

    def __mul__(self, other):

        if isinstance(other, Iterable):
            for idx in range(len(other[:self.size()])):
                self[idx] *= other[idx]

        else:
            for idx in range(len(self)):
                self[idx] *= other

    def get_head(self):
        return self.__head

    def set_head(self, node):
        self.__head = node

    def insert(self, item, idx=0):
        if idx >= self.size() and self.size() != 0:
            raise IndexError("Index is out of range")

        if self.size() == 0:
            self.set_head(node=SingleNode(item))
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
            self.set_head(node=SingleNode(item))
            self.get_head().set_next(old_head)

            self.__size += 1

    def size(self):
        return self.__size

    def is_empty(self):
        return True if self.size() == 0 else False

    def __find_item(self, item):

        prev = None
        cur = self.get_head()
        nxt = cur.get_next()

        for i, item_i in enumerate(self):

            if item_i == item:
                return prev, cur, nxt, i

            else:
                prev = cur
                cur = nxt
                nxt = nxt.get_next()

    def __find_idx(self, idx):

        prev = None
        cur = self.get_head()
        nxt = cur.get_next()

        for i, item_i in enumerate(self):

            if idx == i:
                return prev, cur, nxt, idx

            else:
                prev = cur
                cur = nxt
                nxt = nxt.get_next()

    def delete(self, item=None):

        if item is None:
            return

        elif item is not None:
            prev, cur, nxt, idx = self.__find_item(item=item)

            if prev is not None:
                prev.set_next(nxt)

            elif prev is None:
                self.set_head(nxt)

    def pop(self, idx):

        if idx < 0 or idx >= self.size():
            raise IndexError

        prev, cur, nxt, i = self.__find_idx(idx)

        if prev is not None:
            prev.set_next(nxt)
            return cur.get_item()

        elif prev is None:
            self.set_head(nxt)
            return cur.get_item()

    @staticmethod
    def __mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            L = arr[:mid]  # Dividing the array elements
            R = arr[mid:]  # into 2 halves

            SinglyLinkedList.__mergeSort(L)  # Sorting the first half
            SinglyLinkedList.__mergeSort(R)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    @staticmethod
    def __partition(arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def __quickSort(arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = SinglyLinkedList.__partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            SinglyLinkedList.__quickSort(arr, low, pi - 1)
            SinglyLinkedList.__quickSort(arr, pi + 1, high)

    def sort(self, method, order='+'):

        if method == 'insertion':

            for i in range(1, self.size()):

                item = self[i]

                j = i - 1
                while j >= 0 and item < self[j]:
                    self[j+1] = self[j]
                    j -= 1
                self[j+1] = item

        elif method == 'selection':

            for i in range(self.size()):

                min_idx = i

                for j in range(i+1, self.size()):
                    if self[min_idx] > self[j]:
                        min_idx = j

                self[i], self[min_idx] = self[min_idx], self[i]

        elif method == 'merge':

            self.__mergeSort(self)

        elif method == 'quick':

            self.__quickSort(self, 0, self.size()-1)

    def reverse(self):
        return self.__reversed__()


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


SLL = SinglyLinkedList([np.random.randint(0, 10) for _ in range(10)])
print(SLL)

SLL*[1,2,3,4,5,6,7,8,9,10]
print(SLL)