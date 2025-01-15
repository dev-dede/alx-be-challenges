#Dictionary of information on my favorite book
favorite_book = dict({"author": "Harper Lee", "title": "To kill a Mockingbird", "genre": "fiction"})

#Retrieve genre of book using genre keyword like you would do in a list
print(favorite_book["genre"])

#Retrieve genre of book using the .get method
print(favorite_book.get("genre"))