from twitter.twitter_api import TwitterAPI
from chatgpt.chatgpt_api import ChatGPTAPI
import configparser
import random
import time

def lambda_handler(event, context):
    """
    Lambda trigger that gets triggered by an EventBridge rule to send a tweet
    """
    try:
        # Generate a random sleep duration between 1 and 5 minutes (60 to 300 seconds)
        # We are sleeping to add a bit of randomness between our tweet times everyday.
        sleep_duration = random.randint(60, 300)

        # Sleep for the generated duration
        time.sleep(sleep_duration)
        generate_tweet()

    except Exception as e:
        return {
            'statusCode': 200,
            'body': 'Tweet Successfull!'
        }


def generate_tweet():
    """
    Function that initializes clients and tweet's a ChatGPT generated Tweet.
    """
    # Create a ConfigParser object
    twitter_config = configparser.ConfigParser()
    chatgpt_config = configparser.ConfigParser()

    # Read the 'config.ini' file
    twitter_config.read('twitter_config.ini')
    chatgpt_config.read('chatgpt_config.ini')

    chatgpt_client = ChatGPTAPI(api_key=chatgpt_config["API"]["api_key"])
    gpt_response = chatgpt_client.generate_response()

    twitter_client = TwitterAPI(
        consumer_key=twitter_config["API"]["consumer_key"],
        consumer_secret=twitter_config["API"]["consumer_secret"],
        access_token=twitter_config["API"]["access_token"],
        access_token_secret=twitter_config["API"]["access_token_secret"]
    )

    twitter_client.create_tweet(gpt_response)

def main():
    generate_tweet()

if __name__ == '__main__':
    main()

