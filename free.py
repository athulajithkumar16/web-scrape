import requests
from bs4 import BeautifulSoup

res = requests.get('https://codedamn.com')

# txt = res.text
# status = res.status_code

soup = BeautifulSoup(res.content,'html.parser')

h1 = []
for i in soup.select('h1'):
    h1.append(i.text)

print(h1)
# firsth1 = soup.select('h1')[0].text
# print(firsth1)

# title = soup.title.text
# body = soup.body.text
# head = soup.head.text

# print(title)
# print(body)
# print(head)

# print()
# print(txt,status)