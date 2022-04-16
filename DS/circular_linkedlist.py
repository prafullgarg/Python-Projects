class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedlist:
    """This is an circular linked list class which will create an linked list which is linked 
       from head and tail means next pointer of tail pointing to head """
    def __init__(self):
        self.head=None
    def append(self,node):
        if self.head==None:
            
            self.head=node
            node.next=self.head
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            temp.next=node
            node.next=self.head
    def insert(self,node):
        if self.head==None:
            self.head=node
            node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=node
            node.next=self.head
            self.head=node
            
            
    def __str__(self):
        if self.head==None:
            return "["+"]"
        else:
            string=""
            temp=self.head
        
            while temp.next is not self.head:
                temp=temp.next
                string+= f"{temp.data}" +"-->"
  
            return string
    def pop(self):
        if self.head==None:
            raise IndexError("list is empty")
        else:
            temp=self.head
            while temp.next.next!=self.head:
                temp=temp.next
            data=temp.next.data
            temp.next=self.head
        return data
    def delh(self):
        if self.head==None:
            raise IndexError("list is empty")
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
    def search(self,val):
        if self.head==None:
            raise IndexError("list is empty")
        else:
            temp=self.head
            while temp.next!=self.head:
                if temp.data==val:
                    return temp
            return None
            
