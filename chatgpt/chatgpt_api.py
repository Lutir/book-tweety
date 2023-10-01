import openai
from chatgpt.constants import ChatGPTConstants as Constants

class ChatGPTAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.engine = "gpt-3.5-turbo"
    
    def generate_response(self, prompt):
        openai.api_key = self.api_key
        
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages = [
                {"role": "system", "content": f"{Constants.SYSTEM_ROLE_MSG}"},
                {"role": "user", "content": f"{Constants.USER_ROLE_MSG}"},
            ]
        )
        return response['choices'][0]['message']['content'].strip('"')       