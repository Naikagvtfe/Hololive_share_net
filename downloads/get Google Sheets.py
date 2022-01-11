import requests as rq
from bs4 import BeautifulSoup
import requests

link = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vSfU8OZvASbRtNsY7kvvYohRZOEzrkRRSGlhbbWIbSogfmTf_mGpAvvnG4KofL-jEgy-hX7t8WQJBCW/pubhtml?gid=19040749&amp;single=true&amp;widget=true&amp;headers=false")

def gethtml(rooturl, encoding="utf-8"):
    response = rq.get(rooturl)
    response.encoding = encoding
    html = response.text
    return html 
    
html = gethtml(link)
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('td',dir="ltr")

for tag in a_tags:
    print(tag.string)