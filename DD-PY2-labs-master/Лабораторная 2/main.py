class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages
    def __str__(self):
        return 'Книга "' +self.name+'"'
    def __repr__(self):
        return f"Book({self.id},{self.name}, {self.pages})"

class Library:
    def __init__(self, books=[]):
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return len(self.books)

    def get_index_by_book_id(self, bookname):
        index = 0
        for i in self.books:
            if i.name == bookname:
                index = i.id
        if index == 0:
            raise ValueError(f'книга "{bookname}" отсутствует')
        return index



