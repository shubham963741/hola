from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")

bsObj = BeautifulSoup(html.read(),"html.parser")

for links in bsObj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^(\/wiki\/)((?!:).)*$")}):
    if "href" in links.attrs:
        print(links.attrs["href"])