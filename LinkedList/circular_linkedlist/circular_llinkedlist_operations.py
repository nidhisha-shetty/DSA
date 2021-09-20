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

    def addAfter(self, data, item):
        temp = Node(data)
        p = self.a.next
        while p:
            if (p.data == item):
                temp.next = p.next
                p.next = temp
            if (p == self.a):
                self.a = temp
                return self.a
            else:
                return self.a
            p = p.next
            if (p == self.a.next):
                print(item, "not present in the list")
                break
            
ll=LinkedList()
ll.addToEmpty(3)
ll.addBegin(5)
ll.addEnd(7)
ll.addAfter(9, 5)
ll.traverse()
