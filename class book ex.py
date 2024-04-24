class Book:
    def __init__(self,title,quantity,author,price):
        self.title=title
        self.quantity=quantity
        self.author=author
        self.price=price
        
    def __repr__(self):
        return f"book:{self.title},quantity:{self.quantity},author:{self.author},price:{self.price}"
book1=Book('Book 1',12,'author 1',120)
book2=Book('Book 2',18,'author 2',220)
book3=Book('Book 3',22,'author 3',320)
    
print(book1)
print(book2)
print(book3)