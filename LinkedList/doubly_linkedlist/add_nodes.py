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
        while temp!=None:
            print("node: "+str(temp.data))
            temp=temp.next
    '''
    Add start node
    #1->2->3
    #0->1->2->3
    '''
    def add_start_node(self, data):
        new_node=Node(data)
        new_node.next=self.head
        new_node.prev=None
        self.head.prev=new_node
        self.head=new_node
    '''
    Add a node after a given node
    #1->2->3
    #1->2->4->3
    '''
    def insertAfter(self, cur_data, next_data):
        temp=self.head 
        while temp.data!=cur_data:
            # print(temp.data)    
            temp=temp.next 
        after_node=Node(next_data)
        temp.next.prev=after_node
        after_node.next=temp.next 
        temp.next=after_node
        after_node.prev=temp
    '''
    Add a node before a given node
    #1->2->4->3
    #1->6->2->4->3
    '''
    def insertBefore(self, cur_data, before_data):
        temp=self.head 
        while temp.next.data!=cur_data:
            temp=temp.next
        before_node=Node(before_data) 
        temp.next.prev=before_node
        before_node.next=temp.next
        temp.next=before_node
        before_node.prev=temp  
    '''
    Add node at end
    #1->6->2->4->3
    #1->6->2->4->3->10
    '''
    def end_node(self, end_data):
        temp=self.head 
        while temp.next!=None:
            temp=temp.next
        end_node=Node(end_data)    
        temp.next=end_node
        end_node.prev=temp

ll=Linkedlist()
ll.head=Node(1)
ll.b=Node(2)
ll.c=Node(3) 

ll.head.next=ll.b 
ll.b.next=ll.c 

ll.add_start_node(0)
ll.insertAfter(2,4)
ll.insertBefore(2,6)
ll.end_node(10)
ll.traverse()
