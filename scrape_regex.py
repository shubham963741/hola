from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)

bsObj = BeautifulSoup(html.read(),"html.parser")


images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})

for image in images:
    print(image["src"])