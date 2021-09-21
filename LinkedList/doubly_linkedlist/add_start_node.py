class Node:
    def __init__(self,data):
        self.next=None 
        self.prev=None
        self.data=data 

class Linkedlist:
    def __init__(self):
        self.head=None 
    def traverse(self):
        temp=self.head 
        while temp!=None:
            print("node: "+str(temp.data))
            temp=temp.next
    
    def add_start_node(self, data):
        new_node=Node(data)
        new_node.next=self.head
        new_node.prev=None
        self.head.prev=new_node
        self.head=new_node

ll=Linkedlist()
ll.head=Node(1)
ll.b=Node(2)
ll.c=Node(3) 

ll.head.next=ll.b 
ll.b.next=ll.c 

ll.add_start_node(0)
ll.traverse()
