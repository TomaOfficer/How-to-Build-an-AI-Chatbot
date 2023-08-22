from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    url = request.form['url']
    response = requests.get(url)

    if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")
      timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
      directory = "data"
      if not os.path.exists(directory):
        os.makedirs(directory)
      filename = os.path.join(directory, f'output_{timestamp}.html')

      with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))

      return f"HTML content saved to {filename}"
    else:
      return f"Error: Status code {response.status_code}"

  return render_template('index.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
