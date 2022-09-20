import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://lapinozpizza.in/store-locator/Indore"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

foods=[]
table = soup.find('div', attrs = {'class':'card-wrap'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'store-wrap'}):
    food = {}
    food['title'] = row.h2.text
    food['url'] = row.a['href']
    food['img'] = row.img['src']
    food['address'] = row.p.text
    food['alt_text'] = row.img['alt']
    food['location'] = row.li.text
    #food['time'] = row.li.last.text
    foods.append(food)

filename = 'foods_list1.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','url','img','address','alt_text','location'])
    w.writeheader()
    for food in foods:
        w.writerow(food)

print("Successfully csv file generated")