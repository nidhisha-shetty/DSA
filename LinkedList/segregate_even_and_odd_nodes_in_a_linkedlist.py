#using array
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None
    
    def traverse(self):
        arr=[]
        arr_odd=[]
        arr_even=[]
        temp=self.a
        while temp!=None:
            print(temp.data)
            arr.append(temp.data)
            temp=temp.next
        
        for node in arr:
            if node%2==0:
                arr_even.append(node)
            else:
                arr_odd.append(node)
        arr_even.extend(arr_odd)
        
        #returns result in array
        print(arr_even)#returns result in array
        
        #returns result in linkedlist
        newlist=Node(0)
        for node in arr_even:      
            newlist.next=Node(node)
            newlist=newlist.next
            print(newlist.data)

ll=LinkedList()
ll.a=Node(8)
ll.b=Node(12)
ll.c=Node(10)
ll.d=Node(5)
ll.e=Node(4)
ll.f=Node(1)
ll.g=Node(6)

ll.a.next=ll.b
ll.b.next=ll.c
ll.c.next=ll.d
ll.d.next=ll.e
ll.e.next=ll.f
ll.f.next=ll.g

ll.traverse()
