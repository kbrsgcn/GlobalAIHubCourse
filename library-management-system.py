class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def ListBooks(self):
        self.file.seek(0)
        bookContents = self.file.read()
        contentLines = bookContents.splitlines()
        i = 1
        for line in contentLines:
            bookDetail = line.split(",")
            print("Book -",i)
            print("Book Title: ",bookDetail[0], "\nAuthor Name: ",bookDetail[1],"\n")
            i += 1

    def AddBook(self):
        bookTitle = input("Please enter the title of the book: ")
        bookAuthor = input("Please enter the author of the book: ")
        releaseYear = input("Please enter the release year of the book: ")
        numPages = input("Please enter the number of pages of the book: ")

        bookDetail = f"{bookTitle},{bookAuthor},{releaseYear},{numPages}\n"

        self.file.write(bookDetail)

    def DeleteBook(self):
        bookTitle = input("Please enter the title of the book that you want to remove: ")
        self.file.seek(0)
        bookContents = self.file.read()
        contentLines = bookContents.splitlines()
        newBookFile = []
        for book in contentLines:
            if not book.startswith(bookTitle): #We're searching through title becuase we first write the title of the book in each line
                newBookFile.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(newBookFile)
        print("\nThe book with the title", bookTitle, "removed successfully from your library.")
        

lib = Library()

while True:
    print("\n---- Kubra's Library ----\n")
    print("1- List Books")
    print("2- Add a Book")
    print("3- Remove a Book")
    userInput = input("Please enter your choice: ")

    if userInput == '1':
        print("\n-----List of all the books-----\n")
        lib.ListBooks()
        print("\n-----List of all the books-----\n")
    elif userInput == '2':
        lib.AddBook()
    elif userInput == '3':
        lib.DeleteBook()
    else:
        print("You've entered an invalid number. Please enter 1, 2 or 3")

