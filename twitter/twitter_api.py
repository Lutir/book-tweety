import tweepy

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        """
        Initialize the TwitterAPI client with credentials.

        :param consumer_key: Twitter API consumer key
        :param consumer_secret: Twitter API consumer secret
        :param access_token: Twitter API access token
        :param access_token_secret: Twitter API access token secret
        """
        # Setting up credentials
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        # Set up Tweepy API client
        self.api = tweepy.Client("", consumer_key, consumer_secret, access_token, access_token_secret)

    def create_tweet(self, message):
        """
        Sends a tweet via TwitterAPI client
        """
        response = self.api.create_tweet(text=message)
        print(f"Create Tweet response is {response}")

