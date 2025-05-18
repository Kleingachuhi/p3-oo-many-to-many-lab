class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book: 'Book', date: str, royalties: int):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])



class Book:
    all = []
    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Author must be an instance of the author class")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Book must be an instance of the book class")
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("Date must be a string")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("Royalty must  be an instance  of the Contract class")
        Contract.all.append(self)
        

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

book = Book("Title")
author = Author("Name")
date = '01/01/2001'
royalties = 40000
contract = Contract(author, book, date, royalties)