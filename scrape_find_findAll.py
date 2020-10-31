from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/warandpeace.html"

html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

a = bsObj.findAll({"h1","h2","h3"})                     #tags
b = bsObj.findAll("span" , {"class":{"green","red"}})   #attributes (uses or filter)
c = bsObj.findAll(text="the prince")                    #text
d = bsObj.findAll(id="title")                           #keywords

print(a)
print("-----------------------------------------------------------------")
print(b)
print("-----------------------------------------------------------------")
print(c)
print("-----------------------------------------------------------------")
print(d)
