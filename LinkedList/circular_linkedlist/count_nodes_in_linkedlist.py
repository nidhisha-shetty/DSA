'''
P.S: Count the number of nodes in circular linkedlist
'''

#Solution:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None

    def hasCycle(self):
        count=0
        head=self.a
        fast=slow=head
        if head==None:
            return False
        if head.next==None:
            return False
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
            count+=1
            if fast==slow:
                print(count)
                break
        
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

ll.hasCycle()
