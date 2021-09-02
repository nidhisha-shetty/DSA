'''
P.S: Remove a node from Circular LinkedList
'''

#Solution:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None

    def remove(self,val):
        head=self.a
        temp=head
        while temp.next.data!=val:
            temp=temp.next
        temp.next=temp.next.next
        
            
ll=LinkedList()

ll.a=Node(1)
ll.b=Node(2)
ll.c=Node(3)
ll.d=Node(4)
ll.e=Node(5)
ll.f=Node(6)
ll.g=Node(7)

ll.a.next=ll.b
ll.b.next=ll.c
ll.c.next=ll.d 
ll.d.next=ll.e
ll.e.next=ll.f  #making linkedlist circular
ll.f.next=ll.g
ll.g.next=ll.a

ll.remove(5)
