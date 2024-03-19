import os
from groq import Groq
from flask import Flask, request, jsonify, render_template
import pdfplumber

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
      for page in pdf.pages:
          text += page.extract_text()
    return text

# Path to your PDF file
pdf_path = "The_Constitution_of_Kenya_2010.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form['user_message']
    context=pdf_text
    # Generate bot response for the given prompt
    chat_completion = client.chat.completions.create(
    messages=[
        {"role":context},
        {"role": "user", "content": prompt}],
    max_tokens=500,
    model="mixtral-8x7b-32768"
)

    # Extract bot response from the completion
    bot_response = chat_completion.choices[0].message.content

    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(port=81, host="0.0.0.0", debug=True)
