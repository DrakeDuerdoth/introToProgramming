
#Assignment Four

#Problem One

class Book (object):
    '''a class of book information from the library'''

    libraryName = '---Cooler Sounding DePaul Library---'
    
    def __init__(self, bookTitle = 'unset',
                auth = 'unset',
                bookEdition = -1,
                co = False):
        
        self.title = bookTitle
        self.author = auth
        self.edition = bookEdition
        self.checkedOut = co

    def checkOut(self):
        self.checkedOut = 'Yes'

    def returnBook(self):
        self.checkedOut = 'No'

    def __eq__(self,otherBook):
        self.title = self.title.lower()
        self.author = self.author.lower()
        if self.title == otherBook.title and\
        self.author == otherBook.author:
            return True
        else:
            return False
         
    def __str__(self):
        '''returns all information for the book'''

        if self.checkedOut is False:
            self.checkedOut = 'No'
        else:
            self.checkedOut = 'Yes'

        bookInfo = '{}\n \tBook: {} \n \tAuthor: {} \n \
\tEdition: {} \n \tChecked Out? {}\n'.format(self.libraryName,
        self.title, self.author, self.edition, self.checkedOut)
        return bookInfo
