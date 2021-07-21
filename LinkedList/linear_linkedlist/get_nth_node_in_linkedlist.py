'''
P.S: Write a function to get Nth node in a Linked List using iterative and recursive methods
'''
#iterative way
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None 
    def get_node_data(self, index):
        temp=self.a 
        count=0
        while temp!=None:
            
            if count==index:
                return temp.data 
            else:
                count+=1
                temp=temp.next
        return "Invalid index"

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

print(ll.get_node_data(0))

#recursive way
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None
        self.count=0 
        
    def get_node_data(self, index):
        while self.a!=None:
            if self.count==index:
                return self.a.data
            else:
                self.count+=1             
                self.a=self.a.next
                self.get_node_data(index)

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

print(ll.get_node_data(3))
