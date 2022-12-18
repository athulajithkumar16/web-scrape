import requests
from bs4 import BeautifulSoup


test = "https://webscraper.io/test-sites/e-commerce/allinone"

res = requests.get(test)

soup = BeautifulSoup(res.content,"html.parser")

tag = soup.body
if soup=="GeForce GTX 1050":
    print('Available')

# for string in tag.strings:
#     print(string)