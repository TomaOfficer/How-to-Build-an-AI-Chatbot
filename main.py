import requests
from bs4 import BeautifulSoup

# Input the URL
url = input("Please enter the URL: ")

# Fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.text, "html.parser")

  # Open the file in write mode
  with open('output.html', 'w', encoding='utf-8') as file:
    # Write the HTML content to the file
    file.write(str(soup))

  # Print a success message
  print("HTML content saved to output.html")
else:
  print(f"Error: Status code {response.status_code}")
