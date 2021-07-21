#using linkedlist
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None
    
    def traverse(self):
        odd_test=odd=Node(0)  
        even_test=even=Node(0)
        temp=Node(0)
        temp=self.a
        while temp!=None:
            if temp.data%2==0:
                even.next=Node(temp.data)
                even=even.next
                temp=temp.next
            else:
                odd.next=Node(temp.data)
                odd=odd.next
                temp=temp.next
        
        while even_test.next!=None:
            print(even_test.next.data)
            even_test=even_test.next
        while odd_test.next!=None:
            print(odd_test.next.data)
            odd_test=odd_test.next

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
