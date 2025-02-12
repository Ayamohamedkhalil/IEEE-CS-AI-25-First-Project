booksDictionary = dict()
filePath ="Library_management_database.txt"



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

