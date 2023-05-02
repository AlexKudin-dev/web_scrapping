import requests
import bs4
from headers import headers

response = requests.get('https://habr.com/ru/all/',headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')

for articl in articles:
  art_time = articl.find('time')
  art = articl.find('h2').find('a')
  href = art['href']
  url = 'https://habr.com' + href
  print(f"{art_time.text}\n{art.text}\n{url}")
  print('-----------')
