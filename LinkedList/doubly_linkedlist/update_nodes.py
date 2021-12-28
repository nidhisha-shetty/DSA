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
#         prev=self.head
#         while temp!=None:
#             # print("prev node"+str(prev.data))
#             print("node: "+str(temp.data))
#             prev=temp
#             temp=temp.next

#     def update_middle(self, cur_data, new_data):
#         temp=self.head
#         while temp!=None:
#             if temp.data==cur_data:
#                 temp.data=new_data 
#             temp=temp.next

#     def update_last(self, new_data):
#         temp=self.head 
#         while temp.next!=None:
#             temp=temp.next
#         temp.data=new_data

#     def update_first(self, new_data):
#         self.head.data=new_data

# ll=Linkedlist()
# ll.head=Node(1)
# ll.b=Node(2)
# ll.c=Node(3) 
# ll.d=Node(4)
# ll.e=Node(5)
# ll.f=Node(6)
# ll.g=Node(7)

# ll.head.next=ll.b 
# ll.b.next=ll.c 
# ll.c.next=ll.d
# ll.d.next=ll.e
# ll.e.next=ll.f 
# ll.f.next=ll.g

# ll.update_middle(5,15)
# ll.update_last(100)
# ll.update_first(0)
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

    def update_node(self, old_data, new_data):
        node = self.head
        while node.data != old_data:
            node=node.next
        node.data=new_data
            
    def node_iter(self):
        node = self.head
        while node:
            yield node
            # print("nodes", node.data)
            node = node.next

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.data, self.node_iter()))        
    
