import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_ward():
  messages = [{
      "role":
      "system",
      "content":
      "You are a chatbot naned Ward that reluctantly answers questions"
  }]

  while True:
    user_input = input("You: ")

    messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2,
        max_tokens=4000,
    )

    ward_message = completion.choices[0].message["content"]
    print(f"Ward: {ward_message}")

    messages.append({"role": "assistant", "content": ward_message})


if __name__ == "__main__":
  chat_with_ward()

# from flask import Flask, render_template, request
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#   if request.method == 'POST':
#     url = request.form['url']
#     response = requests.get(url)

#     if response.status_code == 200:
#       soup = BeautifulSoup(response.text, "html.parser")
#       timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#       directory = "data"
#       if not os.path.exists(directory):
#         os.makedirs(directory)
#       filename = os.path.join(directory, f'output_{timestamp}.html')

#       with open(filename, 'w', encoding='utf-8') as file:
#         file.write(str(soup))

#       return f"HTML content saved to {filename}"
#     else:
#       return f"Error: Status code {response.status_code}"

#   return render_template('index.html')

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=8080)
