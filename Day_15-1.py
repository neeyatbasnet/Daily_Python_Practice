from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
url=input("Enter url:")

for i in range(7):
    
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')

    tags=soup('a')
    url=tags[17].get('href',None)
tag_name=tags[17].contents
print(tag_name)
