# class Node:
#     def __init__(self,data):
#         self.next=None 
#         self.prev=None
#         self.data=data 

# class Linkedlist:
#     def __init__(self):
#         self.head=None 
#     def traverse(self):
#         temp=self.head 
#         while temp!=None:
#             print("node: "+str(temp.data))
#             temp=temp.next
#     '''
#     Add start node
#     #1->2->3
#     #0->1->2->3
#     '''
#     def add_start_node(self, data):
#         new_node=Node(data)
#         new_node.next=self.head
#         new_node.prev=None
#         self.head.prev=new_node
#         self.head=new_node
#     '''
#     Add a node after a given node
#     #1->2->3
#     #1->2->4->3
#     '''
#     def insertAfter(self, cur_data, next_data):
#         temp=self.head 
#         while temp.data!=cur_data:
#             # print(temp.data)    
#             temp=temp.next 
#         after_node=Node(next_data)
#         temp.next.prev=after_node
#         after_node.next=temp.next 
#         temp.next=after_node
#         after_node.prev=temp
#     '''
#     Add a node before a given node
#     #1->2->4->3
#     #1->6->2->4->3
#     '''
#     def insertBefore(self, cur_data, before_data):
#         temp=self.head 
#         while temp.next.data!=cur_data:
#             temp=temp.next
#         before_node=Node(before_data) 
#         temp.next.prev=before_node
#         before_node.next=temp.next
#         temp.next=before_node
#         before_node.prev=temp  
#     '''
#     Add node at end
#     #1->6->2->4->3
#     #1->6->2->4->3->10
#     '''
#     def end_node(self, end_data):
#         temp=self.head 
#         while temp.next!=None:
#             temp=temp.next
#         end_node=Node(end_data)    
#         temp.next=end_node
#         end_node.prev=temp

# ll=Linkedlist()
# ll.head=Node(1)
# ll.b=Node(2)
# ll.c=Node(3) 

# ll.head.next=ll.b 
# ll.b.next=ll.c 

# ll.add_start_node(0)
# ll.insertAfter(2,4)
# ll.insertBefore(2,6)
# ll.end_node(10)
# ll.traverse()


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
