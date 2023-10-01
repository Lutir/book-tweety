import random

class ChatGPTConstants:

    # TODO: Add them in some config that is more configurable
    BOOK_NAME = "Deep Work"
    AUTHOR_NAME = "Cal Newport"

    SYSTEM_ROLE_MSG = f"From '{BOOK_NAME}' by '{AUTHOR_NAME},' I'd like 14 unique insights presented as engaging tweets. Tweets number 1, 5, 7 and 9 should convey the impression that I discovered the facts or insights while reading the book by the author, and include the Book Name and Author Name. Each tweet should be concise, informative (280 characters max), and include 5 relevant hashtags at the end related to the book's content. Later when I ask you in the format 'Tweet Number XYZ' you should reply me with the tweet related to that key learning."

    USER_ROLE_MSG = f"Tweet Number {random.randint(1, 13)}"