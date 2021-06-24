class Node:
    def __init__(self, data):
        self.data = data #Assign data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.a = None  

    def printlist(self):
        temp=self.a    
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def removefirstnode(self):
        if self.a==None:
            print("Lonkedlist is empty")
        else:
            self.a=self.a.next

    def removelastnode(self):
        node=self.a
        while node.next.next!=None:
            node=node.next
        node.next=None

    def removebetnode(self, nodecheck):
        if self.a==None:
            print("Linkedlist is empty")
        else:
            node=self.a
            while node.next.data!=nodecheck:
                node=node.next
            node.next=node.next.next

ll=LinkedList()

ll.a=Node(1)
ll.b=Node(2)
ll.c=Node(3)
ll.d=Node(4)
ll.e=Node(5)
ll.f=Node(6)

ll.a.next=ll.b
ll.b.next=ll.c
ll.c.next=ll.d
ll.d.next=ll.e
ll.e.next=ll.f

ll.printlist()
print("--------")

ll.removefirstnode()
ll.printlist()
print("--------")

ll.removelastnode()
ll.printlist()
print("--------")

ll.removebetnode(4)
ll.printlist()


