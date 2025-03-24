#Weekly code challenge - week 2

# The program creates a tuple of five favorite books.

# A for loop is used to print each book on a separate line

my_tuple =( "The Great Gatsby", "The Catcher in the Rye", "To Kill a Mockingbird", "The Bell Jar", "The Picture of Dorian Gray")

for i, book in enumerate(my_tuple):
  print(i + 1, book, end="\n")