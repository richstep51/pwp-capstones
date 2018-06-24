from TomeRater import *

## coding: utf-8
## Learn Python Capstone Project: TomeRater

#############################################################################
############################# Instance Objects ##############################
#############################################################################
rds = User('Rich', 'rich@gmail.com')
dsr = User('RichieRich', 'rich@gmail.com')
richEeyore = User('Rich', 'rich@gmail.com')
ww2 = Book('World War II at Sea: A Global History', 190243678)
ww3 = Book('World War II at Sea: A Global History', 190243678)
pap = Fiction('Pride and Prejudice', 'Jane Austen', 679783261)
pap2 = Fiction('Pride and Prejudice', 'Jane Austen', 679783261)
man0 = Non_Fiction('The Society of Mind', 'Artificial Intelligence', 'Beginner', 671657135)
man1 = Non_Fiction('On Cooking', 'Culinary', 'Expert', 131713272)
man2 = Non_Fiction('On Cooking', 'Culinary Arts', 'Expert', 131713272)
rater = TomeRater()

print('==================================================================')
print('==================== TESTING TomeRater Class =====================')
print('==================================================================')

##################################### BOOKS #################################
r_ww = rater.create_book('World War II at Sea: A Global History', 190243678)
r_man = rater.create_non_fiction('The Society of Mind', 'Artificial Intelligence', 'Beginner', 671657135)
r_man2 = rater.create_non_fiction('On Cooking', 'Culinary Arts', 'Expert', 131713272)
r_pap = rater.create_novel('Pride and Prejudice', 'Jane Austen', 679783261)
para = rater.create_novel('The Parasite', 'Arthur Conan Doyle', 809594374)

#################################### USERS ##################################
rater.add_user('RDSgmail', 'rds@gmail.com', user_books = [r_ww, r_pap, r_man])
rater.add_user('RDShotmail', 'rds@hotmail.com')
rater.add_user('RDSYahoo', 'rds@yahoo.com')

############################### BOOKS TO USERS ##############################
rater.add_book_to_user(r_man2, 'rds@hotmail.com', 3)
rater.add_book_to_user(r_man2, 'rds@yahoo.com', 4)
rater.add_book_to_user(para, 'rds@gmail.com', 4)
rater.add_book_to_user(para, 'rds@hotmail.com', 3)

#############################################################################
print('\n--------------------- Error Handling Checks ----------------------')
rater.add_book_to_user(r_man2, 'rds@gmail.com', 5)
rater.add_book_to_user(r_man, 'mistake@msn.com')
rater.add_book_to_user(para, 'rds@yahoo.com', -1)

#############################################################################
print('\n-------------------- TomeRater User Community --------------------')
for user in rater.users:
    print('{value}'.format(
          value = rater.users[user]
    ))

#############################################################################
print('\n----------------------- TomeRater Library ------------------------')
for book in rater.books:
    print('Book: {book} - read by {count}'.format(
          book  = book
        , count = rater.books[book]
    ))

#############################################################################
print('\n--------------------- TomeRater Catalog List ---------------------')
rater.print_catalog()

#############################################################################
print('\n----------------------- TomeRater User List ----------------------')
rater.print_users()

#############################################################################
print('\n------------------------- Most Read Book -------------------------')
book = rater.get_most_read_book()
print('{book} : read by {count}'.format(
      book  = repr(book)
    , count = rater.books[book]
))

#############################################################################
print('\n----------------------- Highest Rated Book -----------------------')
book = rater.highest_rated_book()
print('{book} : rating = {rate}'.format(
      book = book
    , rate = book.get_average_rating()
))

#############################################################################
print('\n----------------------- Most Positive User -----------------------')
user = rater.most_positive_user()
print('{user} : rating = {rate}'.format(
      user = user
    , rate = user.get_average_rating()
))

# ###########################################################################
# ########## code below is used for a LIST of highest-rated books ###########
# ###########################################################################
# print('\n---------------------- Highest Rated Book(s) ---------------------')
# highest = rater.highest_rated_book()
# for book in highest:
#     print('{book} : rating = {rate}'.format(
#           book = book
#         , rate = book.get_average_rating()
#     ))
#  
# ###########################################################################
# ############ code below is used for a LIST of most-read books #############
# ###########################################################################
# print('\n------------------------ Most Read Book(s) -----------------------')
# mostread = rater.get_most_read_book()
# for book in mostread:
#     print('{book} : read by {count}'.format(
#           book  = book
#         , count = rater.books[book]
#     ))
# 
# ###########################################################################
# ########## code below is used for a LIST of most-positive users ###########
# ###########################################################################
# print('\n---------------------- Most Positive User(s) ---------------------')
# high_users = rater.most_positive_user()
# for user in high_users:
#     print('{user} : rating = {rate}'.format(
#           user = user
#         , rate = user.get_average_rating()
#     ))
# 

print('==================================================================')
print('======================= TESTING User Class =======================')
print('==================================================================')

#############################################################################
print('\n-------------------- Class Equality Checks ---------------------')
print('\tIs rds the same as richEeyore? {boo}'.format(boo = rds == richEeyore))
if rds == richEeyore:
    rds.change_email('rich@msn.com')
print('\tIs rds the same as richEeyore? {boo}'.format(boo = rds == richEeyore))
print('\tIs rds the same as dsr? {boo}'.format(boo = rds == dsr))

#############################################################################
print('\n-------------- List Community Users with repr() call -------------')
community = [rds, dsr, richEeyore]
for user in community:
    print('\t{user}'.format(user = repr(user)))

#############################################################################
print('\n--------------- List Community Users directly (str) --------------')
for user in community:
    print('\t{user}'.format(user = user))

#############################################################################
print('\n--------------- List Community Users Email Accounts --------------')
for user in community:
    print('\t{email}'.format(email = user.get_email()))

#############################################################################
print('\n-------------------- Test User Reading Ratings -------------------')
print(  '    -------------------- Entry Error Checks ------------------')
dsr.read_book(man1, -1)
dsr.read_book(man1, 5)
print(  '    ------- Valid Entries and get_average_rating Tests -------')
rds.read_book(ww2)
rds.read_book(pap, 3)
rds.read_book(man1, 3)
rds.read_book(man0, 4)
print('The average book rating for {user} is {avg}'.format(
      user = rds
    , avg = str(rds.get_average_rating())[:4]
    ))

print('==================================================================')
print('======================= TESTING Book Class =======================')
print('==================================================================')

#############################################################################
print('\n----------------------- Add Book Ratings -----------------------')
print(  '    -------------------- Entry Error Checks ------------------')
ww2.add_rating(-1)
ww2.add_rating(5)
print(  '    ------- Valid Entries and get_average_rating Tests -------')
ww2.add_rating(0)
ww2.add_rating(1)
ww2.add_rating(2)
ww2.add_rating(3)
ww2.add_rating(4)
ww2.add_rating(3.5)
print('\tThe average book rating for {book} is {avg}'.format(
      book = ww2
    , avg = str(ww2.get_average_rating())[:4]
    ))

#############################################################################
print('\n-------------------- Class Equality Checks ---------------------')
print('\tIs ww2 the same as ww3? {boo}'.format(boo = ww2 == ww3))
ww3.set_isbn(19024367)
print('\tIs ww2 the same as ww3? {boo}'.format(boo = ww2 == ww3))

#############################################################################
library = [pap, ww2, ww3]
print('\n----------------- Books in the library (repr) ------------------')
for book in library:
    print('\t{book}'.format(book = repr(book)))

#############################################################################
print('\n------------------ Books in the library (str) ------------------')
for book in library:
    print('\t{book}'.format(book = book))

#############################################################################
print('\n------------------ Library Titles (get_title) ------------------')
for book in library:
    print('\t{title}'.format(title=book.get_title()))

#############################################################################
print('\n------------------- Library ISBNs (get_isbn) -------------------')
for book in library:
    print('\t{isbn}'.format(isbn=str(book.get_isbn()).zfill(10)))

print('==================================================================')
print('===================== TESTING Fiction Class ======================')
print('==================================================================')

#############################################################################
print('\n------------------ Fiction Get Functions Test ------------------')
print('\t"{book}" (ISBN:{isbn}) was written by {author}.'.format(
      book   = pap.get_title()
    , isbn   = str(pap.get_isbn()).zfill(10)
    , author = pap.get_author()
      ))

#############################################################################
print('\n----------------------- Add Book Ratings -----------------------')
print(  '    -------------------- Entry Error Checks ------------------')
pap.add_rating(-1)
pap.add_rating(5)
print(  '    ------- Valid Entries and get_average_rating Tests -------')
pap.add_rating(0)
pap.add_rating(1)
pap.add_rating(2)
pap.add_rating(3)
pap.add_rating(4)
pap.add_rating(3.5)
print('\tThe average book rating for {book} is {avg}'.format(
      book = pap
    , avg = str(pap.get_average_rating())[:4]
    ))

#############################################################################
print('\n-------------------- Class Equality Checks ---------------------')
print('\tIs pap the same as pap2? {boo}'.format(boo = pap == pap2))
pap.set_isbn(67978326)
print('\tIs pap the same as pap2? {boo}'.format(boo = pap == pap2))
library = [pap, pap2]

#############################################################################
print('\n----------------- Books in the library (repr) ------------------')
for book in library:
    print('\t{book}'.format(book=repr(book)))

#############################################################################
print('\n------------------ Books in the library (str) ------------------')
for book in library:
    print('\t{book}'.format(book=book))

#############################################################################
print('\n------------------ Library Titles (get_title) ------------------')
for book in library:
    print('\t{title}'.format(title=book.get_title()))

#############################################################################
print('\n------------------- Library ISBNs (get_isbn) -------------------')
for book in library:
    print('\t{isbn}'.format(isbn=str(book.get_isbn()).zfill(10)))

#############################################################################
print('\n----------------- Library Authors (get_author) -----------------')
for book in library:
    print('\t{isbn}'.format(isbn=book.get_author()))

print('==================================================================')
print('=================== TESTING Non-Fiction Class ====================')
print('==================================================================')

#############################################################################
print('\n----------------------- Add Book Ratings -----------------------')
print(  '    -------------------- Entry Error Checks ------------------')
man2.add_rating(-1)
man2.add_rating(5)
print(  '    ------- Valid Entries and get_average_rating Tests -------')
man2.add_rating(0)
man2.add_rating(1)
man2.add_rating(2)
man2.add_rating(3)
man2.add_rating(4)
man2.add_rating(3.5)
print('\tThe average book rating for {book} is {avg}'.format(
      book = man2
    , avg = str(man2.get_average_rating())[:4]
    ))

#############################################################################
print('\n-------------------- Class Equality Checks ---------------------')
print('\tIs man1 the same as man2? {boo}'.format(boo = man1 == man2))
man2.set_isbn(13171327)
print('\tIs man1 the same as man2? {boo}'.format(boo = man1 == man2))

#############################################################################
print('\n----------------- Books in the library (repr) ------------------')
library = [man0, man1, man2]
for book in library:
    print('\t{book}'.format(book=repr(book)))

#############################################################################
print('\n------------------ Books in the library (str) ------------------')
for book in library:
    print('\t{book}'.format(book=book))

#############################################################################
print('\n------------------ Library Titles (get_title) ------------------')
for book in library:
    print('\t{title}'.format(title=book.get_title()))

#############################################################################
print('\n------------------- Library ISBNs (get_isbn) -------------------')
for book in library:
    print('\t{isbn}'.format(isbn=str(book.get_isbn()).zfill(10)))

#############################################################################
print('\n------------------ Library Levels (get_level) ------------------')
for book in library:
    print('\t{isbn}'.format(isbn=book.get_level()))

#############################################################################
print('\n---------------- Library Subjects (get_subject) ----------------')
for book in library:
    print('\t{isbn}'.format(isbn=book.get_subject()))
##################################################################
