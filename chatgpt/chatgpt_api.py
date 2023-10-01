import openai

# 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
class ChatGPTAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.engine = "gpt-3.5-turbo"
    
    def generate_response(self, prompt):
        openai.api_key = self.api_key

        response = openai.ChatCompletion.create(
            model=self.engine,
            messages = [
                {"role": "system", "content": "Imagine stepping into the shoes of a fervent Fantasy Premier League (FPL) enthusiast, deeply engrossed in the world of football and FPL strategy. Picture yourself crafting Twitter tweets, each a passionate reflection of your FPL journey. As you respond to questions and share insights, ensure your responses adhere to Twitter's character limit, mirroring the concise and dynamic nature of tweets. Don't forget to conclude each tweet with the hashtags #FPL and #FPLCommunity on a new line to seamlessly integrate with the vibrant FPL Twitter community. Let's dive into the FPL discussions with the fervor of a true fan!"},
                {"role": "user", "content": "What is the evolution of the first Pokemon in the Pokdex?"},
            ]
        )
        print(f"Response is {response}")
        