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

    def delete_node(self, old_data):
        node = self.head
        while node.next.data != old_data:
            node = node.next
        next_node = node.next.next
        node.next = next_node
    
    def delete_first_node(self):        
        self.head = self.head.next

    def delete_last_node(self):        
        node = self.head
        while node.next.next != None:
            node = node.next
        node.next = None
        
    def node_iter(self):
        node = self.head
        while node:
            yield node
            print("nodes", node.data)
            node = node.next

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.data, self.node_iter()))
