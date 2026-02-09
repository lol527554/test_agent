from flask import Flask, request, jsonify
from agent import ChatAgent
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY environment variable not set")

# Initialize the chat agent
chat_agent = ChatAgent(api_key)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Missing 'message' field in request body"}), 400

    user_message = data['message']
    try:
        response = chat_agent.get_response(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Chat API! Use the /chat endpoint to interact with the chatbot."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)