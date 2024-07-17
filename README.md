# Examiner Chatbot

Examiner Chatbot is a Flask-based web application that interacts with Wikipedia and the Groq API to provide summaries and generate quizzes based on user input.

## Features

- Search Wikipedia for information based on user input
- Summarize Wikipedia articles
- Generate quiz questions from the summarized content

## Requirements

- Python 3.x
- Flask
- Requests
- Groq API key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/examiner-chatbot.git
    cd examiner-chatbot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Groq API key as an environment variable:

    ```bash
    export GROQ_API_KEY='your_groq_api_key'
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://localhost:81` to use the chatbot.

## File Structure

- `app.py`: The main Flask application file.
- `requirements.txt`: List of Python dependencies.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files (CSS, JS).

## Functionality

- **Home Page**: Displays the main interface where users can enter their questions.
- **Query Wikipedia**: Searches Wikipedia for the user's query and retrieves the relevant snippet.
- **Summarize**: Uses the Groq API to summarize the Wikipedia snippet.
- **Generate Quiz**: Creates quiz questions based on the summarized content.

## Example

1. Enter a query such as "Kenyan Constitution" into the input field.
2. The chatbot searches Wikipedia and retrieves a summary.
3. The chatbot generates quiz questions based on the summary and displays them.

## License

This project is licensed under the MIT License.

