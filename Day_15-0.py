from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
sum=0

url=input("Enter url:")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('span')
for tag in tags:
    for num in tag.contents:
        num=int(num)
        sum=sum+num
print("Sum:",sum)