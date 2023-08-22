import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Input the URL
url = input("Please enter the URL: ")

# Fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.text, "html.parser")

  # Generate a unique filename with a timestamp
  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
  filename = f'output_{timestamp}.html'

  # Open the file in write mode
  with open(filename, 'w', encoding='utf-8') as file:
    # Write the HTML content to the file
    file.write(str(soup))

  # Print a success message
  print("HTML content saved to {filename}")
else:
  print(f"Error: Status code {response.status_code}")
