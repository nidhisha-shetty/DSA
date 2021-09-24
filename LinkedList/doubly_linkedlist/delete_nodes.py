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
    
    def delete_start_node(self, del_data):
        del_node=Node(del_data)
        temp=self.head
        if self.head.data==del_node.data:
            self.head=temp.next
            temp.next.prev=None

ll=Linkedlist()
ll.head=Node(1)
ll.b=Node(2)
ll.c=Node(3) 

ll.head.next=ll.b 
ll.b.next=ll.c 

ll.delete_start_node(1)
ll.traverse()
