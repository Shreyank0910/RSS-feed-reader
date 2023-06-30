from bs4 import BeautifulSoup
import requests

url = requests.get('https://realpython.com/atom.xml')

content = BeautifulSoup(url.content, 'xml')
entries = content.find_all('entry')

for entry in entries:
  title = entry.title.text
  summary = entry.summary.text
  link = entry.link['href']
  print(f"Title: {title}\n\nSummary: {summary}\n\nLink: {link}\n\n ..............................\n\n")    