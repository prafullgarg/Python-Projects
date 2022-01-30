class IndexOutOfBoundError(Exception):
    pass
class DyanArray:
    """DyanArray class for dynamic array  implementation in python"""
    def __init__(self,size):
        self.__size=size
        self.__array=[None for _ in range(size)]
        self.__head=-1 #head is index of current element 
    def __str__(self):
        items=""
        for element in self.__array:
            if not element is None:
                items+=str(element) +","
            else:
                break
        return f"[{items}]"
    def is_full(self):
        if self.__head==self.__size-1:
            return True
        return False
    def __resize_array(self): #timecomplexcity O(n)
        """This method  provide dynamic size allocation to array""" 
        new_array=[None for _ in range(2*self.__size)]
        for i in range(self.__size):
            new_array[i]=self.__array[i]
        self.__size=2*self.__size
        self.__array=new_array
    def __lshift(self,index):#timecomplexcity O(n)
        """private method shift used to shift elements from location index of array by one position forward """
        ub=self.__head+1
        self.__head+=1
        while ub!=index:
            self.__array[ub]=self.__array[ub-1]
            ub-=1
    def __rshift(self,index):#timecomplexcity O(n)
        """private method shift used to shift elements from location index of array by one position backward """
        while index<self.__head:
            self.__array[index]=self.__array[index+1]
            index+=1
            self.__head-=1
    def append(self,data): #timecomplexcity O(1)
        """this is an effective append function with time complexcity of O(1)  \nand appends element at the end of array"""
        if self.is_full():
            self.__resize_array()
        self.__head+=1
        self.__array[self.__head]=data
    def insert(self,index,data):#timecomplexcity O(n)
        """This method insert data at location index """
        if 0<=index<=self.__size-1:
            if self.is_full():
                self.__resize_array()
            else:
                self.__lshift(index)
                self.__array[index]=data
        else:
            if index<0:
                raise IndexOutOfBoundError(f"Negative indexing is not allowed in array")
            else:
                raise IndexOutOfBoundError(f"Array  index {index} dose not exist")
    def pop(self,loc=None):#timecomplexcity O(1) when loc==None ,O(n) when loc !=None
        """By default This function will delete last element of array\n if location is given then it will delete data at given location """
        if loc is None:
            self.__array[self.__head]=None
            self.__head-=1
        else:
            ele=self.__array[loc]
            self.__rshift(loc)
    @property
    def array(self): #get property for array
        return self.__array
    @property # 
    def size(self): #get property for array size
        return self.__size
