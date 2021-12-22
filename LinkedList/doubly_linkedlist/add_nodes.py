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
        
    def insertAfter(self, prev_node, new_data):    # [12, 8, 2, 5] -> [12, 8, 2, 4, 5]
        node = self.head
        while node and node.data != prev_node:
            node = node.next

        if node:
            new_node = Node(new_data)    
            node_next = node.next
            node.next = new_node 
            new_node.prev=node   
            new_node.next = node_next
            node_next.prev = new_node
            
    def insertBefore(self, next_node, new_data):    # [12, 8, 2, 5] -> [12, 8, 2, 4, 5]
        node = self.head
        while node.next and node.next.data != next_node:
            node = node.next
            print(node.data)
        if node:
            new_node = Node(new_data)
            next_node=node.next
            new_node.next=node.next
            new_node.prev=node
            next_node.prev=new_node
            node.next=new_node
            
    def insertLast(self, last_node):
        new_node = Node(last_node)
        node = self.head
        while node.next!=None:
            node=node.next
        node.next=new_node 
        
    def node_iter(self):
        node = self.head
        while node:
            yield node
            print("nodes", node)
            node = node.next

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.data, self.node_iter()))
