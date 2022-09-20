import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.dailypioneer.com/"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

foods=[]
#table = soup.find('div', attrs = {'class':'row'}) 
   
for row in soup.findAll('div',
                         attrs = {'class':'row topStoryList no-gutters'}):
    food = {}
    food['title'] = row.h3.text
    #food['description'] = row.p.text
    #food['icon']= row.i
    food['url'] = row.a['href']
    food['img'] = row.img['src']
    food['alt_text'] = row.img['alt']
    # food['location'] = row.li.text
    #food['time'] = row.li.last.text
    foods.append(food)
    
    

filename = 'the_pioneer_news.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','url','img','alt_text'])
    w.writeheader()
    for food in foods:
        w.writerow(food)

print("Successfully csv file generated")