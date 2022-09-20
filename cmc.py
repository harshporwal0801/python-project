import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://cmccareer.in/"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

foods=[]
#table = soup.find('div', attrs = {'class':'row'}) 
   
for row in soup.findAll('div',
                         attrs = {'class':'col-md-3 col-sm-3 fdsrrf'}):
    food = {}
    #food['title'] = row.h2.text
    food['description'] = row.p.text
    food['icon']= row.i
    #food['url'] = row.a['href']
    #food['img'] = row.img['img src']
    # food['alt_text'] = row.img['alt']
    # food['location'] = row.li.text
    #food['time'] = row.li.last.text
    foods.append(food)
    

filename = 'cmc1.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','description','icon'])
    w.writeheader()
    for food in foods:
        w.writerow(food)

print("Successfully csv file generated")