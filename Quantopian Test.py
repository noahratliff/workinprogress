from bs4 import BeautifulSoup
import requests

hot = requests.get('https://www.reddit.com/hot/', headers = {'User-agent': 'your bot 0.1'})
print(hot.text)
