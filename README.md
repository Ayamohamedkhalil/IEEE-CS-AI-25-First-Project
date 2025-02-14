# IEEE-CS-AI-25-First-Project

The Library Management System is a console-based Python application designed to efficiently manage a library's inventory of books. It allows users to perform various operations such as adding, viewing, searching, updating, and deleting book records, as well as saving and loading the data to and from a file. This system ensures data consistency and integrity through comprehensive validation checks and error handling. 


1-Add Book:

Allows the user to add a new book with the following details:
.Book ID (Unique Identifier)
.Title
.Author
.Publication Year

Validations:
.Book ID: Must be unique, non-empty, and non-whitespace.
.Title: Cannot be empty or whitespace.
.Author: Must contain alphabetic characters only.
.Publication Year: Must be a positive integer and not exceed the current year (2025).

2-View Books:

.Displays a list of all books stored in the system.
.If no books are present, it displays an appropriate message.

3-Search Book:

.Enables searching for a book by either its ID or Title.
.Case-insensitive search for book titles.
.Displays the complete details of the book if found, or a "Book Not Found" message if not.

4-Update Book Details:

.Allows updating of existing book details by searching via Book ID or Title.
.Prompts the user to enter new values for Book ID, Title, Author, and Publication Year.
.Validates the new inputs to ensure data integrity.
.If the Book ID is changed, it ensures uniqueness before updating the records.

5-Delete Book:

.Deletes a book from the system by Book ID.
.Displays an appropriate message if the book is not found.


6-Save to File:

.Saves the current list of books to an external text file (Library_management_database.txt).
.Each book entry is formatted for easy readability and retrieval.


7-Load from File:

.Loads books from the external text file into the system.
.Handles potential errors like file not found, invalid format, and duplicate IDs.
.Skips invalid entries while displaying appropriate warnings.

8-Exit:

.Safely exits the system.
