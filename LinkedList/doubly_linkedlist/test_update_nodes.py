import pytest

from doubly_linked_list_update import Linkedlist

class TestLinkedlist:
    
    def setup_method(self):
        """[12, 8, 2, 5]"""
        self.prepared_linked_list = Linkedlist()
        self.prepared_linked_list.add_start_node(5)
        self.prepared_linked_list.add_start_node(2)
        self.prepared_linked_list.add_start_node(8)
        self.prepared_linked_list.add_start_node(12)
        # self.prepared_linked_list.insertAfter(2,6)
        assert list(self.prepared_linked_list) == [12, 8, 2, 5]
    
    def test_update_node(self):
        self.prepared_linked_list.update_node(8, 7)
        assert list(self.prepared_linked_list) == [12, 7, 2, 5]
        
    def test_update_first_node(self):
        self.prepared_linked_list.update_first_node(0)
        assert list(self.prepared_linked_list) == [0, 8, 2, 5]

    def test_update_last_node(self):
        self.prepared_linked_list.update_last_node(9)
        assert list(self.prepared_linked_list) == [12, 8, 2, 9]
