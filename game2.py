class library:
     def __init__(self):
         self.noBooks = 0
         self.books = []
    
     def addBooks(self, book) :
           self.books.append(book)
           self.noBooks = len(self.books)
     def showinfo(self) :
         print(f"the library has {self.noBooks} books are ")
         for book in self.books:
             print(book)
         
         
a=library()
a.addBooks("THE GREAT PRINCE ")
a.addBooks(" GREAT PRINCE ")
a.addBooks("  PRINCE ")
a.addBooks("hard work prince")
a.showinfo()
             