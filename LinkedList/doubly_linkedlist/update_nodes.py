class Node:
    def __init__(self,data):
        self.next=None 
        self.prev=None
        self.data=data 

class Linkedlist:
    def __init__(self):
        self.head=None 

    def add_start_node(self, data):
        new_node=Node(data)
        if self.head != None: 
            new_node.next=self.head
            new_node.prev=None
            self.head.prev=new_node
            self.head=new_node
        else: # If the list is empty, make new node both head and tail
            self.head = new_node
            self.tail = new_node
            new_node.prev = None # There's only one element so both pointers refer to null
            new_node.next = None
            
    def update_first_node(self, new_data):
        node = self.head
        node.data=new_data
        
    def update_node(self, old_data, new_data):
        node = self.head
        while node.data != old_data:
            node=node.next
        node.data=new_data
            
    def update_last_node(self, new_data):
        node = self.head
        while node.next != None:
            node=node.next
        node.data=new_data
        
    def node_iter(self):
        node = self.head
        while node:
            yield node
            print("nodes", node.data)
            node = node.next

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.data, self.node_iter()))        
    
