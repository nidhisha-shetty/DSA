class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.a=None
    
    def traverse(self):
        head=self.a
        temp=head
        while temp!=None:
            print(temp.data)
            temp=temp.next
    
    def addToEmpty(self, data):

		# Creating the newnode new
        new = Node(data)
        self.a = new
    
    def addBegin(self, data):
        temp = Node(data)
        temp.next = self.a.next
        self.a.next = temp
        return self.a	
    
    def addEnd(self, data):
        temp = Node(data)
        print(self.a.data)
        temp.next = self.a.next
        self.a.next = temp
        self.a = temp
        # print(self.a.data)
        return self.a
    
            
ll=LinkedList()
ll.addToEmpty(3)
ll.addBegin(5)
ll.addEnd(7)
ll.traverse()
