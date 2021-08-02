import requests
from bs4 import BeautifulSoup

url='https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
el = soup.find('h3').text.strip()
print(el)