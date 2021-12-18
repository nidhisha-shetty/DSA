import pytest

from doubly_linked_list import Linkedlist

class TestLinkedlist:
    def setup_method(self):
        """[12, 8, 2, 5]"""
        self.prepared_linked_list = Linkedlist()
        self.prepared_linked_list.add_start_node(5)
        self.prepared_linked_list.add_start_node(2)
        self.prepared_linked_list.add_start_node(8)
        self.prepared_linked_list.add_start_node(12)

        assert list(self.prepared_linked_list) == [12, 8, 2, 5]

    def test_add_start_node(self):
        linked_list = Linkedlist()

        linked_list.add_start_node(1)
        assert list(linked_list) == [1]

        linked_list.add_start_node(3)
        assert list(linked_list) == [3, 1]

        linked_list.add_start_node(5)
        assert list(linked_list) == [5, 3, 1]

        linked_list.add_start_node(4)
        assert list(linked_list) == [4, 5, 3, 1]
        
    def test_insertAfter(self):
        self.prepared_linked_list.insertAfter(2, 4)
        assert list(self.prepared_linked_list) == [12, 8, 2, 4, 5]
    
    def test_insertBefore(self):
        self.prepared_linked_list.insertBefore(5, 4)
        assert list(self.prepared_linked_list) == [12, 8, 2, 4, 5]
        
    def test_insertLast(self):
        self.prepared_linked_list.insertLast(8)
        assert list(self.prepared_linked_list) == [12, 8, 2, 5, 8]
