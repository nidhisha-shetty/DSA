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

    #Delete the first node of the LnkedList        
    def removefirstnode(self):
        if self.a==None:
            print("Lonkedlist is empty")
        else:
            self.a=self.a.next
            
    #Delete the last node of the LnkedList  
    def removelastnode(self):
        node=self.a
        while node.next.next!=None:
            node=node.next
        node.next=None

    #Delete a specific node from the LnkedList  
    def removebetnode(self, nodecheck):
        if self.a==None:
            print("Linkedlist is empty")
        else:
            node=self.a
            while node.next.data!=nodecheck:
                node=node.next
            node.next=node.next.next

ll=LinkedList()

#Creating nodes in the linkedlist
ll.a=Node(1)
ll.b=Node(2)
ll.c=Node(3)
ll.d=Node(4)
ll.e=Node(5)
ll.f=Node(6)

#Connecting the nodes in the linkedlist
ll.a.next=ll.b
ll.b.next=ll.c
ll.c.next=ll.d
ll.d.next=ll.e
ll.e.next=ll.f

ll.printlist() #Prints the complete linkedlist

ll.removefirstnode() 
ll.printlist() #Prints the linkedlist except first node
print("--------")

ll.removelastnode()
ll.printlist() #Prints the linkedlist except first and last node 
print("--------")

ll.removebetnode(4)
ll.printlist() #Prints the linkedlist except first, last, and the node with value 4
