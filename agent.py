import openai

class ChatAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_response(self, message):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            raise RuntimeError(f"Failed to get response from LLM: {e}")