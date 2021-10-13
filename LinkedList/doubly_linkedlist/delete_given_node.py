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
    def delete_node(self, pos):
        count=0
        temp=self.head
        while count<pos:
            temp=temp.next
            count+=1
        
        temp.next.prev=temp.prev
        temp.prev.next=temp.next

   
ll=Linkedlist()
ll.head=Node(1)
ll.b=Node(2)
ll.c=Node(3) 
ll.d=Node(4)
ll.e=Node(5)
ll.f=Node(6)
ll.g=Node(7)

ll.head.next=ll.b 
ll.b.next=ll.c 
ll.c.next=ll.d
ll.d.next=ll.e
ll.e.next=ll.f 
ll.f.next=ll.g 

ll.delete_node(2)
ll.traverse()
