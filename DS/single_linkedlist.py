
class IndexError(Exception):
    pass
class EmptyListError(Exception):
    pass
class node:
    """This is an node class which contain two fields one for data of node and another for address of next node in the list. 
       node is an list element"""
    
    def __init__(self,data):
        """values initialized"""
        self.data=data
        self.next=None
                    
class linkedlist:
    """This class constructor will always create a new linked list whenever called."""
    def __init__(self):
        """This is an class constructor which will instantiate the object of class"""
        self.head=None
        self.tail=None
        self.last_second=None

    def isempty(self):
        """This function will return true is list has atleast one node
           else it will return false"""
        return self.head==None
    
    def last_second_node(self):
        temp=self.head
        while temp.next.next!=None:
                temp=temp.next
        self.last_second=temp
        
    def append_n(self,node):
        """This is an append function which will append node in linked list in O(n) time because it will iterate over
           linked list until it reaches the last node then it will assign new node to the next pointer of last node and 
           assign  newly add node as last node"""
        if self.isempty():
            self.head=node
            self.tail=node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node
            self.tail=node          
            
        
    def append_one(self,node):
        """This is also an append function which will execute in O(1) time complexity
           where self.tail.next represents the last node's next pointer
           and self.tail resonates last node. 
           """
        if self.isempty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        
    def __str__(self):
        if self.isempty():
            return "[]"
        else:
            temp=self.head
            result=f"{self.head.data}"
            while temp.next!=None:
                temp=temp.next
                result=result+ "-->"+ f"{temp.data}"
                
            return result
        
    def insertion_at_beginning(self,node):
        """This function will insert  node at the beginning of the linked list"""
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
            
    def indexing(self):
        i=0
        while self.head!=None:
            setattr(self.head,index,i)
            i+=1
    def insertion_at_position(self,prev_data,node):
        """This fuction will search for data and insert the node after the searched node"""
        if self.isempty():
            raise IndexError("list is empty can't insert")
        else:
            temp=self.head
            while temp.data!= prev_data:
                temp=temp.next
            node.next=temp.next
            temp.next=node
    def pop_at_end(self):
        """This method deletes the last node in O(n) time"""
        if self.isempty():
            raise EmptyListError("List is empty no element can be poped")

        else:
            self.last_second_node()
            self.last_second.next=None
    def deletion_at_position(self,data):
        """This method will delete the node with first occurence of matching data from the list"""
        if self.isempty():
            raise EmptyListError("list is empty")
        else:
            temp=self.head
            while temp.next.data!=data:
                temp=temp.next
            temp.next=temp.next.next
            
    def find(self,data):
        """This method will give boolean value if node exists in list then true else false"""
        temp=self.head
        while temp.next!=None:
            if temp.data==data:
                return True
            temp=temp.next
        return False
            
    def update(self,current_data,new_data):
        """This function will update the data of node with new data"""
        temp=self.head
        while temp.data!=current_data:
              temp=temp.next
        if temp.data==current_data:
            temp.data=new_data
        
