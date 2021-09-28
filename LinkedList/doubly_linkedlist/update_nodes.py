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

    def update_middle(self, cur_data, new_data):
        temp=self.head
        while temp!=None:
            if temp.data==cur_data:
                temp.data=new_data 
            temp=temp.next

    def update_last(self, new_data):
        temp=self.head 
        while temp.next!=None:
            temp=temp.next
        temp.data=new_data

    def update_first(self, new_data):
        self.head.data=new_data

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

ll.update_middle(5,15)
ll.update_last(100)
ll.update_first(0)
ll.traverse()
