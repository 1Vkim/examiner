import os
import json
import requests
from flask import Flask,render_template, request, jsonify

#import anthropic
#from openai import OpenAI
from groq import Groq

app = Flask(__name__, static_url_path='/static')


def query_wiki(title):
    S = requests.Session()


    URL = "https://en.wikipedia.org/w/api.php"



    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "search",
        "limit": "1",
        "srsearch": title,
        "prop": "info",
        "inprop": "url|talkid"
    }

    R = S.get(url=URL, params=PARAMS)
    # Parse the JSON data
    data = R.json()
    # Extract the search results from the data
    if "query" in data and "search" in data["query"]:
        pages = data["query"]["search"]
        for page in pages:
            title = page.get("title")
            snippet = page.get("snippet")
            return title, snippet
    else:
        return "No results found"





def summarize(title):


  client = Groq(
      api_key=os.environ["GROQ_API_KEY"],
  )

  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": f"Summarize {query_wiki(title)}",
          }
      ],
      max_tokens=500,
      model="mixtral-8x7b-32768",
  )

  # Extract bot response from the completion
  bot_response = chat_completion.choices[0].message.content

  return bot_response



def gen_quiz(title):


  client = Groq(
      api_key=os.environ["GROQ_API_KEY"],
  )
  summary=summarize(title)


  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content":f"""Generate five questions from the following {summary}. Make sure to include the question in the format: \n1:\t2:""",
          }
      ],
      max_tokens=500,
      model="mixtral-8x7b-32768",
  )

  # Extract bot response from the completion
  bot_response = chat_completion.choices[0].message.content

  return jsonify({'bot_response': bot_response})


@app.route('/')
def home():
    return render_template('index.html')




@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form['user_message']
    if prompt:
        title = prompt
        try:
            query_wiki_result = query_wiki(title)

        except Exception as e:
            return f"An error occured {str(e)}"

        if  query_wiki_result:
            try:
              summary = summarize(title)

            except Exception as e:
                return f"An error occured {str(e)}"

            if summary:
                return gen_quiz(title)

            else:
                return home()


        else:
            return home()




    else:
        return home()

if __name__ == '__main__':
    app.run(port=81, host="0.0.0.0", debug=True)
