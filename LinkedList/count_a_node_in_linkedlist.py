#P.S: Write a function that counts the number of times a given int occurs in a Linked List using iterative and recursive methods

#using iterative method
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.a=None
    def count(self, node):
        check=0
        temp=self.a
        while temp!=None:
            if temp.data==node:
                check+=1
            temp=temp.next
        return check

ll=LinkedList()
ll.a=Node(1)
ll.b=Node(2)
ll.c=Node(1)
ll.d=Node(2)
ll.e=Node(1)
ll.f=Node(3)
ll.g=Node(1)

ll.a.next=ll.b
ll.b.next=ll.c 
ll.c.next=ll.d 
ll.d.next=ll.e
ll.e.next=ll.f
ll.f.next=ll.g

print(ll.count(1))

#using recursive method
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.a=None
        self.check=0 
    def count(self, head, node):
        temp=head
        
        if temp==None:
            return self.check
        if temp.data==node:
            self.check+=1
            temp1=temp.next
            return self.count(temp1, node)
        else:
            temp1=temp.next
            return self.count(temp1, node)
ll=LinkedList()
ll.a=Node(1)
ll.b=Node(2)
ll.c=Node(1)
ll.d=Node(2)
ll.e=Node(1)
ll.f=Node(3)
ll.g=Node(1)

ll.a.next=ll.b
ll.b.next=ll.c 
ll.c.next=ll.d 
ll.d.next=ll.e
ll.e.next=ll.f
ll.f.next=ll.g

print(ll.count(ll.a,1))
