class NegativeIntegerError(ArithmeticError):
    pass
class StackOverflowError(OverflowError):
    pass
class InvalidTypeError(TypeError):
    pass
class StaticArray:
    """
    this is fixed size array implementation in python
    """
    def __init__(self,size,typee=str):
        """
        initialize size and type of array
        default type will be string
        """
        try:
            if size<0:
                   raise NegativeIntegerError("Negative size is not allowed")
            self.__size=size
            self.__data=[None for _ in range(size)]
            self.__head=-1
            self.__type=typee
        except TypeError:
            print("provide an integer size")
            
    def __str__(self):
        item=""
        for i in self.__data:
            if i!= None:
                item = item +f"{i}" +","
        return item
    def is_full(self):
        """
        returns true if array is full
        return false if array if is not full 
        """
        if self.__head==self.__size-1:
            return True
        return False
    def is_empty(self):
        if self.__head==-1:
            return True
        return False
    
    def __rshift(self,loc):
        """
        This function will shift all elements after location  loc by 1 shift forward
        """
        if self.is_full():
            raise StackOverflowError("Array is full")
        ptr=self.__head+1
        while ptr>loc:
            self.__data[ptr]=self.__data[ptr-1]
            ptr-=1
    
    def __lshift(self,loc):
        """
        This function will shift all  elements after location loc  backward by 1 shift
        """
        if self.is_empty():
            raise StackUnderflowError("array is empty")
        while loc<self.__head:
            self.__data[loc]=self.__data[loc+1]
            loc+=1
    def __type_check(self,data):
        """
        if the type of the element matchs the type of array then\nthis functionwill return True else false
        """
        if type(data)==self.__type:
            return True
        return False
    
    def append(self,data):
        """
        add element at the end of array with time complexity of O(1)
        """
        if self.is_full():
            raise StackOverflowError("Array is full")
        if not self.__type_check(data):
            raise InvalidTypeError(f"Array is of type {self.__type}")
            
        self.__head+=1
        self.__data[self.__head]=data
    def insert(self,loc,data):
        """
        This will insert element at specified location with time coomplexity of O(n) 
        """
        if not self.__type_check(data):
            raise InvalidTypeError(f"Array is of type {self.__type}")
        self.__rshift(loc)
        self.__data[loc]=data
        self.__head+=1
    def pop(self,loc=None):
        if loc==None:
            self.__data[self.__head]=None
            self.__head-=1
        else:
            if loc<0:
                raise IndexError("negative index not allowed")
            self.__lshift(loc)
            self.__data[self.__head]=None
            self.__head-=1
    def update(self,loc,data):
        """
        modify element at specified location
        """
        if loc<0:
            raise IndexError("negative index not allowed")
        if not self.__type_check(data):
            raise InvalidTypeError(f"Array is of type {self.__type}")
        self.__data[loc]=data
    def index(self,data):
        """
        linear search
        return index of first occurence data if exits
        """
        for i in range(self.__size):
            if self.__data[i]==data:
                return i
