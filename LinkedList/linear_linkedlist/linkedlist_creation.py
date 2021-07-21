class Node: #Creating nodes
    def __init__(self, data):
        self.data=data
        self.next=None
    
class LinkedList: #Creating linkedlist
    def __init__(self):
        self.ptr=None #pointer to linkedlist

ll=LinkedList()

#The LinkedList class contains a reference of Node class type. 
ll.ptr=Node(1) #Initializing nodes with data
ll.b=Node(2)
ll.c=Node(3)
ll.d=Node(4)

ll.ptr.next=ll.b #Connecting nodes
ll.b.next=ll.c 
ll.c.next=ll.d
