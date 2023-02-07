class Book:
    def init(self, author, name):
        self.name = name
        self.__author = author

    def str(self):
        return 'Книга "' +self.name+'"'
    def repr(self):
        return f"Book({self.author},{self.name})"

    def get_name(self):
        return self.__name
    def get_author(self):
        return self.__author

class PaperBook(Book):
    def __init(self, author, name, pages):
        self.author = author
        self.__name = name
        self.set_pages(pages)

    def repr(self):
        return f"PaperBook({self.author},{self.name},{self.pages})"

    def set_pages(self, pages):
        if int == type(pages):
            self.pages = pages
        else:
            raise ValueError("нецелое число страниц")

class AudioBook(Book):
    def __init(self,author,name,duration):
        self.__author = author
        self.__name = name
        self.set_duration(duration)

    def repr(self):
        return f"PaperBook({self.author},{self.name}, {self.duration})"

    def set_duration(self, duration):
        if float == type(duration):
            self.duration = duration
        else:
            raise ValueError("длительность должна иметь тип float")



