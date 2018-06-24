## coding: utf-8
## Learn Python Capstone Project: TomeRater

class User(object):
    def __eq__(self, other_user):
        boo = False
        if type(self) == type(other_user):
            boo = self.name == other_user.name
            boo = boo and self.email == other_user.email
        return boo
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    def __repr__(self):
        num = len(self.books)
        return 'User: {name}, email: {email}, books read: {tot}'.format(
              name  = self.name
            , email = self.email
            , tot   = str(num)
            )
    def __str__(self):
        return 'User: {name}, email: {email}'.format(
              name  = self.name
            , email = self.email
            )
    def change_email(self, new_email):
        self.email = new_email
        print('{user} has a new email address: {email}'.format(
              user  = self.name
            , email = self.email
        ))
    def get_average_rating(self):
        tot = 0
        num = 0
        for value in self.books.values():
            if value != None:
                tot += value
                num += 1
        avg = 0
        if num > 0:
            avg = tot / num
        return avg
    def get_email(self):
        return self.email
    def read_book(self, book, rating = None):
        if rating == None:
            pass
        elif rating >= 0 and rating <= 4:
            self.books[book] = rating
        else:
            print('Invalid Rating: {rate} rating by user {user} is not allowed.\n\tValid: any number between 0 and 4, inclusive.'.format(
                  rate = rating
                , user = self.email
                ))
            self.books[book] = None

class Book(object):
    def __eq__(self, other_book):
        boo = False
        if type(self) == type(other_book):
            boo = self.title == other_book.title
            boo = boo and self.isbn == other_book.isbn
        return boo
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    def __repr__(self):
        return '"{book}"; ISBN: {isbn}; avg rating (num): {avg} ({rtngs})'.format(
              avg   = self.get_average_rating()
            , book  = self.title
            , isbn  = str(self.isbn).zfill(10)
            , rtngs = len(self.ratings)
            )
    def __str__(self):
        return '{book}; ISBN: {isbn}'.format(
              book  = self.title
            , isbn  = str(self.isbn).zfill(10)
            )
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print('Invalid Rating: {rate} rating on book "{book}" is not allowed.\n\tValid: any number between 0 and 4, inclusive.'.format(
                  book = self.title
                , rate = rating
                ))
    def get_average_rating(self):
        rtngs = len(self.ratings)
        tot = 0
        for rating in self.ratings:
            tot += rating
        avg = 0
        if rtngs > 0:
            avg = tot / rtngs
        return avg
    def get_isbn(self):
        return self.isbn
    def get_title(self):
        return self.title
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print('The ISBN number for "{book}" has been changed to {isbn}'.format(
              book = self.title
            , isbn = str(self.isbn).zfill(10)
        ))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def __repr__(self):
        return '"{title}" by {author} (ISBN:{isbn})'.format(
              title  = self.title
            , author = self.author
            , isbn   = str(self.isbn).zfill(10)
            )
    def __str__(self):
        return '{title} by {author}'.format(
              title  = self.title
            , author = self.author
            )
    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def __repr__(self):
        return '"{title}" (ISBN:{isbn})'.format(
              title  = self.title
            , isbn   = str(self.isbn).zfill(10)
            )
    def __str__(self):
        return '{title}, a {level} manual on {subject}'.format(
              level   = self.level
            , subject = self.subject
            , title   = self.title
            )
    def get_level(self):
        return self.level
    def get_subject(self):
        return self.subject

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email)
        if user == None:
            print('No user has email "{email}"'.format(email = email))
        else:
            user.read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            readcount = self.books.get(book)
            if readcount == None:
                self.books[book] = 1
            else:
                self.books[book] = readcount + 1
    def add_user(self, name, email, user_books = None):
        if self.users.get(email) == None:
            self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)
    def create_book(self, title, isbn):
        return Book(title, isbn)
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    def get_most_read_book(self):
        dogear = Book('Nobody is Reading!', 0)
        maxread = 0
        for book in self.books:
            if self.books[book] > maxread:
                dogear = book
                maxread = self.books[book]
        return dogear
    def highest_rated_book(self):
        highest = 0
        hrb = Book('Nobody is Rating Books', 0)
        for book in self.books:
            avg = book.get_average_rating()
            if avg > highest:
                highest = avg
                hrb = book
        return hrb
    def most_positive_user(self):
        maxrate = 0
        posit = User('Least Positive', 'Eeyore@disney.com')
        for key in self.users:
            avg = self.users[key].get_average_rating()
            if avg > maxrate:
                posit = self.users[key]
                maxrate = avg
        return posit
    def print_catalog(self):
        for book in self.books:
            print(book)
    def print_users(self):
        for user in self.users:
            print(self.users[user])
#############################################################################
######  ALTERNATE DEF: code below returns a LIST of highest-rated books #####
#############################################################################
#     def highest_rated_book(self):
#         highest = 0
#         hrb = []
#         for book in self.books:
#             avg = book.get_average_rating()
#             if avg > highest:
#                 highest = avg
#         for book in self.books:
#             if highest == book.get_average_rating():
#                 hrb.append(book)
#         return hrb
#############################################################################
######  ALTERNATE DEF: code below returns a LIST of most-positive users #####
#############################################################################
#    def most_positive_user(self):
#        maxrate = 0
#        posit = []
#        for key in self.users:
#            avg = self.users[key].get_average_rating()
#            if avg > maxrate:
#                maxrate = avg
#        for key in self.users:
#            if maxrate == self.users[key].get_average_rating():
#                posit.append(self.users[key])
#        return posit
#############################################################################
########  ALTERNATE DEF: code below returns a LIST of most-read books #######
#############################################################################
#    def most_read_book(self):
#        dogear = []
#        maxread = 0
#        for book in self.books:
#            if self.books[book] > maxread:
#                maxread = self.books[book]
#        for book in self.books:
#            if self.books[book] == maxread:
#                dogear.append(book)
#        return dogear
