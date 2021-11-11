class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None
    def traverse(self):
        head=self.a
        while head!=None:
            print(head.data)
            head=head.next
    def update(self, existing, new):
        head=self.a
        while head.data!=existing:
            head=head.next
        head.data=new

ll=LinkedList()

ll.a=Node(1)
ll.b=Node(2)
ll.c=Node(3)
ll.d=Node(4)
ll.e=Node(5)

ll.a.next=ll.b
ll.b.next=ll.c
ll.c.next=ll.d 
ll.d.next=ll.e

ll.update(5,7)
ll.traverse()
