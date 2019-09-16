#Defining classes
class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn

    def printBook(self):
        print(self.title + ", " + self.isbn)

def main():
    b1 = Book()
    b2 = Book("Computer Architecture")
    b3 = Book("Accounting")
    b4 = Book("Theory of Programming")

    b1.printBook()
    b2.printBook()
    b3.printBook()
    b4.printBook()

if __name__ == "__main__":
    main()
