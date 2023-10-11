import random
import json

class ChatGPTConstants:
    def __init__(self):
        book_data = self.generate_book_details()
        self.book_name = book_data["book_name"]
        self.author = book_data["author"]

    def get_system_role_prompt(self):
        return f"From '{self.book_name}' by '{self.author},' I'd like 14 unique insights presented as engaging tweets. Tweets number 1, 5, 7 and 9 should convey the impression that I discovered the facts or insights while reading the book by the author, and include the Book Name and Author Name. Each tweet should be concise, informative (280 characters max), and include 5 relevant hashtags at the end related to the book's content. Later when I ask you in the format 'Tweet Number XYZ' you should reply me with the tweet related to that key learning."
    
    def get_user_role_prompt(self):
        return f"Tweet Number {random.randint(1, 13)}"

    def generate_book_details(self):
        books_file_path = "chatgpt/books.json"

        with open(books_file_path, 'r') as books:
            data = json.load(books)
        
        book_number = random.randint(1, 20)
        return data[book_number]