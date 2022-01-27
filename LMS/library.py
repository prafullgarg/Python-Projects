class Admin:
    __books={}
    __instance=None
    def __new__(cls,*args,**kwargs):
        if Admin.__instance==None:
            self=Super(cls,Admin).__new__(cls,*args,**kwargs)
            Admin.__instance=self
            return self
        else:
            return Admin.__instance
    def add_book(self,book):
       

class Reader:
    pass
class Book:
        
    def __init__(self,name,author,count):
        #count --> total number of books available in library
        self.__bname=name
        self.__author=author
        self.__count=count
    def book_details(self):
        return f"Name : {self.__name}\nAuthor : {self.__author}\nBook Available : {self.__count}"
    def set_book_name(self,name):
        self.__bname=name
    def set_book_author(self,author):
        self.__author=author
    def set_book_count(self,count):
        self.__count=count
    def get_book_name(self):
        return self.__bname
    def get_book_name(self):
        return self.__author
    def get_book_name(self):
        return self.__count
