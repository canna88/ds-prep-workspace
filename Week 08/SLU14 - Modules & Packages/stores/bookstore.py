class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)
    
    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"
    
def get_total_price(books):
    total_price = 0
    for book in books:
        total_price += book[2]
    return total_price

description = "this is a module named bookstore"