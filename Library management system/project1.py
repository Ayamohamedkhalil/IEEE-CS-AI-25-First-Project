booksDictionary = dict()
filePath ="Library management system\Library_management_database.txt"

def addBook():
    bookId=input("Enter book Id : ")
    while True:
      if bookId in booksDictionary:  
        print(f"Warning: Duplicate ID {bookId} found. Please enter a unique ID.")
        bookId=input("Enter book Id : ")
      else :
        break  
    title = input("Enter book title: ").strip()  # Remove leading/trailing spaces

    while True:
       if not title.replace(" ", "").isalpha() or title.isspace() or title == "":
        print("Invalid format of book title. Please enter the book title again!")
        title = input("Enter book title: ").strip()
       else:
        break

  

    author=input("Enter book author : ").strip()
    while True:
       if  not author.replace(" ", "").isalpha() or author.isspace() or author == "":
            print("Invalid format of author name,Please Enter The Book Author Again !")
            author=input("Enter book author : ").strip()
       else:
            break

    publicationYear=input("Enter book publication year : ")
    while True:
        if not publicationYear.isnumeric()or int(publicationYear) <= 0 or int(publicationYear) >=2026:
            print("Invalid format of publication year,Please Enter The Book Publication Year Again !")
            publicationYear=input("Enter book publication year : ")
        else:
            break
        
    # genre=input("Enter book genre : ")
    booksDictionary[bookId] = {"title":title, "author":author, "publicationYear":publicationYear}
    print("Book added successfully!")
   


def viewBooks():

    pass


def searchBook():
    pass

def updatebookDetails():
     print("Update ")
    

def deleteBook():
    pass




def loadFromFile():
    global booksDictionary

    try:
        with open(filePath, "r") as myfile:
            data = myfile.read().strip().split("\n\n")  # Read and split books by blank lines
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' was not found.")
        return
    except Exception as e:
        print(f"Unexpected error while reading the file: {e}")
        return

    for book in data:
        try:
            bookDetails = [detail.strip().split(" : ") for detail in book.splitlines()] 
            if len(bookDetails) < 2:  #there is only id give warning and don't save the book
                print(f"Warning: Skipping invalid book entry: {book}")
                continue
            
            bookId = int(bookDetails[0][1])
            if bookId in bookDetails:  # Check dublicate Id's
                print(f"Warning: Duplicate ID {bookId} found. Skipping this entry: {book}")
                continue

            booksDictionary[bookId] = dict(bookDetails[1:])
        
        except ValueError:
            print(f"Error: Invalid book ID format in entry: {book}")
        except IndexError:
            print(f"Error: Missing details in entry: {book}")
        except Exception as e:
            print(f"Unexpected error while processing book entry: {e}")



def saveToFile():

    if len(booksDictionary) == 0:
        print("Warning: No books to save. The file will be empty.")
        return  # Exit if there's nothing to save
    
    try:
        with open(filePath, "w") as myfile:
            # Convert each book entry into a string and write it
            for bookId, details in booksDictionary.items():
                text = f"id : {bookId}\n"
                for key, value in details.items():
                    text += f"{key} : {value}\n"
                text += "\n"  # Add a blank line between books
                
                myfile.write(text)  # Write to file
        print(f"database successfully saved to {filePath}.")
    
    except IOError:
        print(f"Error: Unable to write to {filePath}. Please check file permissions.")
    
    except Exception as e:
        print(f"Unexpected error while saving: {e}")

if __name__ == "__main__":
  while True : 
    print("=====================================================")   
    print("              Library Management System              ")
    print("=====================================================")
    print("1.Add book")
    print("2.View books") 
    print("3.Search to the books (By Id or By book title)")
    print("4.Update book details (By Id or By title) ")
    print("5.Delete book (By Id)")
    print("6.Save to file")
    print("7.Load from file")
    print("8.Exit")
    print("=====================================================")
    option=input("Enter Your Option (1-8) : ")
    match (option):
        case "1":
           addBook()
        case "2":
            viewBooks()
        case "3":
            searchBook()
        case "4":
            updatebookDetails()
        case "5":
            deleteBook()
        case "6":
            loadFromFile()
        case "7":
            saveToFile()
        case "8" :
            print("Exiting from the Library Management System ")    
            break    
        case _:
            print("Invalid option, Please try again !")          