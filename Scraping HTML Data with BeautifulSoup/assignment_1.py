# Sample Data     http://py4e-data.dr-chuck.net/comments_42.html
# Actual Data      http://py4e-data.dr-chuck.net/comments_748749.html 

from urllib import request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html=request.urlopen(url).read()
soup = BeautifulSoup(html)

tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])

print(sum)
