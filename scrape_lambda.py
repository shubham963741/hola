from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"

html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

imageUrl = bsObj.find("img").attrs["src"]
# print(imageUrl)

print(bsObj.findAll(lambda tag: len(tag.attrs)==2))