class node:
    """Since this is and doubly_linked_list which resonates nodes with three fields 
       where each node is having 3 attributes data --> data stored in that node,
       prev --> address of the previous node,next --> address of the next node"""
    def __init__(self,data):
        """Instantiating node with the provide data"""
        self.prev=None
        self.data=data
        self.next=None
class DoublyLinkedList:
    """This is an doubly linked list class who's construtor will create an doubly linked list when called """
    def __init__(self):
        """Instantiating the  Doubly Linked list with default  """
        self.head=None
        self.tail=None
    def display(self,reverse=False):
        """This function will be used to print the linked list in linear for or a sequence
           when reverse is False this function will print list in forward fashion and if it 
           is false then this function will print list in backward fashion"""
        if reverse:
            temp=self.tail
            while temp.prev is not None:
                print(temp.data,end="<--")
                temp=temp.prev
                print(temp.data,end="<--")
                
        else:
            temp=self.head
            while temp.next is not None:
                print(temp.data,end="-->")
        
                temp=temp.next
                print(temp.data,end="-->")
                
       
    def append(self,node):
        """This method will add node at the last of linked list in O(1) time"""
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
    def  insert_at_beginning(self,node):
        """This method is used to insert node at the beginning of the list in O(1) time """
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.head.prev=node
            node.next=self.head
            self.head=node
    def insert_at_position(self,val,node):
        """This method is used to insert node at the specified location"""
        if self.head==None:
            raise IndexError("node dosn,t exists")
        else:
            temp=self.head
            while temp.data!=val:
                temp=temp.next
            node.prev=temp
            node.next=temp.next
            temp.next=node
            node.next.prev=node
    def pop(self):
        """This method will remove the last node from the linked list"""
        if self.head==None:
            raise IndexError("list is empty")
        else:
            data=self.tail.data
            self.tail=self.tail.prev
            self.tail.next=None
            return data
    def pop_at_beginning(self):
        """This method is used to pop the first element from linked list"""
        if self.head==None:
            raise Indexerror("list is empty")
        else:
            data=self.head.data
            self.head=self.head.next
            self.head.prev=None
            return data
    def remove(self,val):
        """This method is used to delete the element from linked list which is equal to the data provide"""
        if self.head==None:
            raise IndexError("list is empty")
            
        elif self.head.data==val:
            self.head=self.head.next
            self.head.prev=None
        else:
            temp=self.head
            while temp.next.data is not val:
                temp=temp.next
            temp.next.next.prev=temp
            temp.next=temp.next.next
    def find(self,val):
        
        """This method is used to search the element from linked list  if element exists in list then
           method will return True else False"""
        if self.head==None:
            raise IndexError("list is empty")
        else:   
            temp=self.head
            while temp.data != val:
                if temp.data is val:
                    return True
                else:
                    return False
                temp=temp.next
            
            
