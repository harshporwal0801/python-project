import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://andaaz-e-shayari.com/posts/hindi-shayari/page/14/'

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

quotes=[]
table = soup.find('div', attrs = {'class:''wrapper'}) 
   
for row in table.findAll('div',
                         attrs = {'class:''entry-title'}):
    quote = {}
    quote['title'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['xmlns']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

filename = 'abhimart1.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','url','xmlns','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

print("Successfully csv file generated")