from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


#response = requests.get("https://oxylabs.io/")
#print(response.text)
url = "http://www.hubertiming.com/results/2017GPTR10K"
#html = urlopen(url)
#soup = BeautifulSoup(url, 'html.parser')
soup = bs(urllib.urlopen(url))
#h3 = (soup.find('div').text)
#records.append(elem.b.text.strip())
#page = requests.get(URL)
#results = soup.find(id="ResultsContainer")
#print(h3)

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(soup.get_text())

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()