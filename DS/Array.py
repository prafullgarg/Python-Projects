class StackOverflowError(OverflowError):
    pass
class IndexOutOfBoundError(Exception):
    pass
class Array:
    """This is Static Array/Fixed size Array"""
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
        """is_full() function returns\nTrue if array is full\nFalse if array has empty space available"""
        if self.__head==self.__size-1:
            return True
        return False
    def append(self,data):
        #this append function has time complexcity is of O(1)
        if self.is_full():
            raise StackOverflowError(f"Array is full cat append {data}")
        self.__head+=1
        self.__array[self.__head]=data
    def insert(self,index,data):
        if 0<=index<=self.__size-1:
            if self.is_full():
                raise StackOverflowError(f"Array is full can't insert {data} at index {index}")
            else:
                ub=self.__head+1
                self.__head+=1
                while ub!=index:
                    self.__array[ub]=self.__array[ub-1]
                    ub-=1
                self.__array[index]=data
        else:
            raise IndexOutOfBoundError(f"Array  index {index} dose not exist")
