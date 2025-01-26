class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"The book titled{self.title} authored by {self.author} has {self.pages} on it"

    def __repr__(self):
        return f"The book (title = '{self.title}' author = '{self.author}' pages = {self.pages}) on it"
    



    book = Book("1984", "Earnest Achayo", 328)
    print(book)
    print(repr(book))