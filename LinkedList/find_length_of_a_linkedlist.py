#using iterative method
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None 
    
class LinkedList:
    def __init__(self):
        self.a=None 
    
    def length(self):
        count=0
        temp=self.a
        while temp!=None:
            count+=1
            temp=temp.next
        return count
            
ll=LinkedList()
ll.a=Node(13)
ll.b=Node(24)
ll.c=Node(33)
ll.d=Node(42)
ll.e=Node(51)
ll.f=Node(62)

ll.a.next=ll.b 
ll.b.next=ll.c 
ll.c.next=ll.d
ll.d.next=ll.e
ll.e.next=ll.f 

print(ll.length())
