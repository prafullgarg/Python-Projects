class StackOverflowError(OverflowError):
    pass
class Array:
    def __init__(self,size):
        self.__size=size
        self.__data=[None for _ in range(size)]
        self.__upperbound=0
    def __str__(self):
        items=""
        for element in self.__data:
            if not element is None:
                items+=str(element) +","
            else:
                break
        return f"[{items}]"
    def append(self,value):
        i=0
        while i<self.__size:
            if self.__data[i] == None:
                self.__data[i]=value
                break
            i+=1
        else:
            raise StackOverflowError(f"Array is full can't append {value}")
        
arr=Array(5)
for i in range(5):
    arr.append(i)
print(arr)
