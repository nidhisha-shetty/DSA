class Node:
    def __init__(self,data):
        self.next=None 
        self.prev=None
        self.data=data 

class Linkedlist:
    def __init__(self):
        self.head=None 

    def traverse_reverse(self):
        li=[]
        temp=self.head 
        while(temp!=None):
            # print(temp.data)
            li.append(temp.data)
            temp=temp.next
        print(li[::-1])
        
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

ll.traverse_reverse()

#without using list
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
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    
    def reverse(self):
        temp = None
        current = self.head
		
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev
        
        
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

ll.reverse()
ll.traverse()
