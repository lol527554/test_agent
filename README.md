# Custom Chat Agent

This repository contains a custom chat agent built using Flask. The agent leverages OpenAI's API to provide intelligent responses to user queries.

## Features
- REST API with endpoints for chat interactions.
- Environment variable support using `dotenv`.
- Easy deployment to cloud platforms.

## Requirements
- Python 3.8+
- Flask
- OpenAI Python SDK

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd custom_agent
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key
     ```

6. Run the server:
   ```bash
   python app.py
   ```

## Endpoints

### `GET /`
- Returns a welcome message.

### `POST /chat`
- Accepts a JSON payload with a `message` field.
- Returns the chatbot's response.

## Deployment

To deploy the application, use platforms like Heroku, AWS, or Render. Ensure to set the `OPENAI_API_KEY` environment variable in the deployment settings.

## License

This project is licensed under the MIT License.