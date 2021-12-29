import pytest

from doubly_linked_list_delete import Linkedlist

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
    
    def test_delete_node(self):
        self.prepared_linked_list.delete_node(8)
        assert list(self.prepared_linked_list) == [12, 2, 5]
    
    def test_delete_first_node(self):
        self.prepared_linked_list.delete_first_node()
        assert list(self.prepared_linked_list) == [8, 2, 5]
    
    def test_delete_last_node(self):
        self.prepared_linked_list.delete_last_node()
        assert list(self.prepared_linked_list) == [12, 8, 2]
