import openai
from chatgpt.constants import ChatGPTConstants as Constants

class ChatGPTAPI:
    def __init__(self, api_key):
        """
        Initialize the ChatGPT client with credentials.

        :param api_key: ChatGPT API Key
        """
        self.api_key = api_key
        self.engine = "gpt-3.5-turbo"
    
    def generate_response(self):
        """
        Generates a response via completion's API for the prompt passed
        """
        openai.api_key = self.api_key
        constants = Constants()
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages = [
                {"role": "system", "content": f"{constants.get_system_role_prompt()}"},
                {"role": "user", "content": f"{constants.get_user_role_prompt()}"},
            ]
        )
        return response['choices'][0]['message']['content'].strip('"')       