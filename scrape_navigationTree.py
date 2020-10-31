from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"

html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)                                                               #prints all the children

# for descendent in bsObj.find("table",{"id":"giftList"}).descendents:
#     print(descendent)                                                          #prints all tags contained

# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)                                                             #prints all the rows except title row

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())         #returns price of item