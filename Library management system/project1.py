booksDictionary = dict()
filePath ="Library management system\\Library_management_database.txt"

def addBook():
    bookId=input("Enter book Id : ").strip()
    while True:
      if not bookId or len(bookId.strip())==0 :
          print("Invalid formar of Id,Please Try again!")
          bookId=input("Enter book Id :").strip()
      elif bookId in booksDictionary:  
        print(f"Warning: Duplicate ID {bookId} found. Please enter a unique ID.")
        bookId=input("Enter book Id : ").strip()
      else :
        break  
    title = input("Enter book title: ").strip() 

    while True:
       if   title == "" or len(title.strip())==0:
        print("Invalid format of book title. Please enter the book title again!")
        title = input("Enter book title: ").strip()
       else:
        break

  

    author=input("Enter book author : ").strip()
    while True:
       if  not author.replace(" ", "").isalpha() or len(author.strip())==0 or author == "":
            print("Invalid format of author name,Please Enter The Book Author Again !")
            author=input("Enter book author : ").strip()
       else:
            break

    publicationYear=input("Enter book publication year : ")
    while True:
        if not publicationYear.isnumeric() or int(publicationYear) <= 0 or int(publicationYear) >=2026 or len(publicationYear.strip())==0 :
            print("Invalid publication year,Please Enter The Book Publication Year Again !")
            publicationYear=input("Enter book publication year : ")
        else:
            break
    booksDictionary[bookId] = {"title":title, "author":author, "publicationYear":publicationYear}
    print("Book added successfully!")
   


def viewBooks():

    if len(booksDictionary) == 0:
        print("No books found in the library.")
    else:
        for bookId, details in booksDictionary.items():
            print(f"Book ID: {bookId}")
            for key, value in details.items():
                print(f"{key}: {value}")
            print()


def searchBook():
    searchKey = input("Enter Book ID or Book Title to search: ").strip()
    
    while not searchKey or len(searchKey.strip()) == 0:  
        print("Invalid input. Please enter a valid Book ID or Title.")
        searchKey = input("Enter Book ID or Book Title to search: ").strip()
    
    found = False
    for bookId, details in booksDictionary.items():
      
        if searchKey == bookId or searchKey.lower() == details["title"].lower():
            print("\nBook found:")
            print("===================================")
            print(f"Book ID         : {bookId}")
            print(f"Book Title      : {details['title']}")
            print(f"Book Author     : {details['author']}")
            print(f"Publication Year: {details['publicationYear']}")
            print("===================================\n")
            found = True
            break
    
    if not found:
        print("Book Not Found.")


def updatebookDetails():

    searchingPoint=input( "Enter Book Id or Book Title : ")
    while True :
        if len(searchingPoint.strip())==0 or searchingPoint == "":
            searchingPoint=input("Please Enter The Right Book Id or Book Title : ")
        else : 
            break
    Found=None
    for book in booksDictionary :
        if searchingPoint == book or searchingPoint == booksDictionary[book]['title']:
            Found=book
            print("Here are the book details :")
            print(f"Book ID: {book}")
            print(f"Title: {booksDictionary[book]['title']}")
            print(f"Author: {booksDictionary[book]['author']}")
            print(f"Publication Year: {booksDictionary[book]['publicationYear']}")
            print()
            break
    if Found is None :
        print("Book Not Found!")
        return    
        
    newBookId = input("Enter New Book ID (press Enter to keep the same): ").strip()
    if newBookId == "" or len(newBookId.strip())==0:
        newBookId = Found
    title = input("Enter New book title: ").strip()  # Remove leading/trailing spaces
    while True:
       if   len(title.strip()) or title == "":
        print("Invalid format of book title. Please enter the book title again!")
        title = input("Enter New book title: ").strip()
       else:
        break

    print("Update book details")
    


    author=input("Enter New book author : ").strip()
    while True:
       if  not author.replace(" ", "").isalpha() or len(author.strip())==0 or author == "":
            print("Invalid format of author name,Please Enter The Book Author Again !")
            author=input("Enter New book author : ").strip()
       else:
            break

    publicationYear=input("Enter New book publication year : ")
    while True:
        if not publicationYear.isnumeric() :
            print("Invalid format of publication year,Please Enter The Book Publication Year Again !")
            publicationYear=input("Enter New book publication year : ")
        elif int(publicationYear) <= 0 or int(publicationYear) >=2026 or len(publicationYear.strip())==0 :
            print("Invalid Range of publication year,Please Enter The Book Publication Year Again!")
            publicationYear=input("Enter book publication year : ")    
        else:
            break

    if newBookId != Found:
        del booksDictionary[Found]  
    booksDictionary[newBookId] = {"title": title, "author": author, "publicationYear": publicationYear}
    print("Book Updated Successfully")  
    
def deleteBook():
    bookId=input("Enter Book Id : ")
    while True :
        if len(bookId) or bookId == "":
            bookId=input("Please Enter The Right Book Id  : ")
        else : 
            break
    if bookId in booksDictionary:
        del booksDictionary[bookId]
        print("Book deleted successfully!")
    else :
        print("Book Is Not Found !")


def loadFromFile():
    global booksDictionary
    booksDictionary = dict()
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
            
            bookId = (bookDetails[0][1])
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
          saveToFile()
        case "7":
            loadFromFile()
        case "8" :
            print("Exiting from the Library Management System ")    
            break    
        case _:
            print("Invalid option, Please try again !")          