class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)
    
    def get_book_info(self):
        print(int(self.price))
        print(self.price)
        return "Title: {0}, Author: {1}, Price: {}.".format(self.title,self.author,int(self.price))

    
    def get_total_price(books):
        total_price = 0
        for book in books:
            total_price += book.price
        return total_price
    
    description = "This is a module named bookstore."