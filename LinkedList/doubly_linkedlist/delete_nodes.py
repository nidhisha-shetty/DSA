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
        prev=self.head
        while temp!=None:
            # print("prev node"+str(prev.data))
            print("node: "+str(temp.data))
            prev=temp
            temp=temp.next
            
    def delete_start_node(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
    
    def delete_before_node(self,data):
        temp=self.head 
        prev=self.head
        while temp.next.data!=data:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp.next.prev=prev 

    def delete_after_node(self,data):
        temp=self.head 
        # prev=self.head
        while temp.data!=data:
            # prev=temp
            temp=temp.next
        temp.next=temp.next.next
        
    def delete_end_node(self):
        temp=self.head
        while temp.next.next!=None:
            # print(temp.next.data)
            temp=temp.next
        # print(temp.data)    
        temp.next=None
        # print(temp)

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

ll.delete_start_node()
ll.delete_before_node(5)
ll.delete_after_node(2)
ll.delete_end_node()
ll.traverse()
