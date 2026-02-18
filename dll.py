#
# Gagnaskipan.
# Double-Linked-List
# Student(s):
#  - Patrik Dagur Sigurðsson

from dll_node import Node
from iterator import NodeIterator

class Position:
    __slots__ = ['node']

    def __init__(self, node : Node):
        self.node = node


class DLList:

    #
    # Beginning of fundamental section.
    #

    def __init__(self):
        self._sentinel_front = Node(None, None, None)
        self._sentinel_back = Node(self._sentinel_front, None, None)
        self._sentinel_front.next = self._sentinel_back
        self._len = 0

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        return NodeIterator(self._sentinel_front.next)


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
        return True if self._len == 0 else False

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        elems = []
        if self.is_empty():
            return "[]"
        node = self._sentinel_front.next
        while node.next is not None:
            elems.append(str(node.item))
            node = node.next
        return '[' + ', '.join(elems) + ']'

    def get_at(self, pos: Position) -> object:
        """
        Return element at position 'pos'.
        :param pos: Position to insert
        :return: Element
        """
        # If the list is empty return None otherwise return the item
        return pos.node.item if not self.is_empty() else None

    def insert_after(self, pos: Position, item: object) -> Position:
        """
        Insert element following position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """

        if pos.node == self._sentinel_back:
            raise IndexError("Out of range")
        # Make the new node
        new_node : Node = Node(prev = pos.node, item = item, next = pos.node.next)
        # Save the next node
        next_node : Node = pos.node.next
        # update pos node
        pos.node.next = new_node
        # update next node
        next_node.prev = new_node
        self._len += 1

        return Position(new_node)

    def insert_before(self, pos: Position, item: object) -> Position:
        """
        Insert element before position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        # Simply insert the item after the node that comes before pos
        if pos.node == self._sentinel_front:
            raise IndexError("Out of range")
        return self.insert_after(Position(pos.node.prev), item)


    def remove(self, pos: Position) -> object:
        """
        Remove element at position 'pos' in the list.
        :param pos: Position of element to remove.
        :return: Element deleted
        """
        if self.is_empty():
            raise IndexError("List is empty")

        next_node : Node = pos.node.next
        prev_node : Node = pos.node.prev

        # Rearrange the pointers
        prev_node.next = next_node
        next_node.prev = prev_node

        self._len -= 1
        return pos.node.item

    def replace(self, pos: Position, item: object) -> object:
        """
        Replace element at position 'pos' in the list.
        :param pos: Position of element to replace
        :param item: New element to replace the existing one.
        :return: The element replaced (formerly at position)
        """
        replaced_item : object = pos.node.item
        pos.node.item = item
        return replaced_item

    def front_pos(self) -> Position | None:
        """
        Return position of the element at the head of the list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return None
        return Position(self._sentinel_front.next)

    def back_pos(self) -> Position | None:
        """
        Return position of the element at the end of list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return None
        return Position(self._sentinel_back.prev)

    def prev_pos(self, pos: Position) -> Position | None:
        """
        Return position before 'pos', or None if already at front of list.
        """
        if pos.node.prev == self._sentinel_front:
            return None
        return Position(pos.node.prev)

    def next_pos(self, pos: Position) -> Position | None:
        """
        Return position following 'pos', or None if already at end of list.
        """
        if pos.node.next == self._sentinel_back:
            return None
        return Position(pos.node.next)

    #
    # End of fundamental section.
    # Implement the methods below by, for the most part, using/calling the ones you have implemented above.
    # Avoid unnecessary code duplication.
    #

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError("List is empty")
        return self.front_pos().node.item

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError("List is empty")
        return self.back_pos().node.item

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        self.insert_after(Position(self._sentinel_front), item)

    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError("List is empty")
        self.remove(self.front_pos())

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        self.insert_before(Position(self._sentinel_back), item)

    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError("List is empty")
        self.remove(self.back_pos())
