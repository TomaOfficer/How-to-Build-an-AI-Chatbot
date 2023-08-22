import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

url = input("Please enter the URL: ")
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

  print(f"HTML content saved to {filename}")
else:
  print(f"Error: Status code {response.status_code}")
