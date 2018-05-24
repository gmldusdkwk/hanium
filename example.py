from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://hankookilbo.com/'
webpage = urlopen(url)
source = BeautifulSoup(webpage, 'lxml')
titles = source.select('article[class=bestNews]')



for i in titles:
    print(i.get_text())
