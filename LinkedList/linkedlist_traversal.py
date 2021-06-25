class Node:
    def __init__(self, data):
        self.data = data #Assign data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.a = None  

    def printlinkedlist(self):
        node=self.a
        while node!=None:  #Traversing the LinkedList
            print(node.data)
            node=node.next

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

ll.printlinkedlist()

