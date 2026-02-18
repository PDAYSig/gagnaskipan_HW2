#
# Gagnaskipan.
# Single-Linked-List
# Student(s):
#  - Patrik Dagur Sigurðsson
#
from sll_node import Node
from iterator import NodeIterator

class SLList:

    def __init__(self):
        """
        Constructor.
        Time complexity: O(1)
        """
        self._head = None
        self._tail = None
        self._len = 0

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        return NodeIterator(self._head)

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        elems = []
        node = self._head
        while node is not None:
            elems.append(str(node.item))
            node = node.next
        return '[' + ', '.join(elems) + ']'

    def __len__(self):
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """
        return self._len

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        return self._head is None  # could alternatively check _tail is None, or _len is 0.

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError('front called on an empty list')
        return self._head.item

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError('back called on an empty list')
        return self._tail.item

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        new_node : Node = Node(item, None)

        if self.is_empty():
            self._head = new_node
            self._tail = self._head

        else:
            new_node.next = self._head
            self._head = new_node
        self._len += 1
    
    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self._head is None:
            raise IndexError("List is empty")

        return_item : Node = self._head.item

        # Change the value of _head and Handle edge case for when there is only one item in the list
        self._head = self._head.next if self._head.next is not None else None
        if self._head == self._tail:
            self._tail = None
        self._len -= 1
        return return_item

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        new_node : Node = Node(item, None)

        if self._tail is None:
            self._head = new_node
            self._tail = self._head

        else:
            self._tail.next = new_node
            self._tail = new_node
        self._len += 1

    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(n)
        :return: None, but trows an exception if list empty.
        """

        if self.is_empty():
            raise IndexError("List is empty")
        
        current_node : Node = self._head
        while current_node.next != self._tail:
            current_node = current_node.next

        self._tail = current_node
        self._tail.next = None
        self._len -= 1
