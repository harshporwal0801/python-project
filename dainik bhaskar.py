import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.bhaskar.com/"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

foods=[]
table = soup.find('div', attrs = {'class':'_28c07b15'}) 
   
for row in soup.findAll('div',
                         attrs = {'class':'_28c07b15'}):
    food = {}
    food['title'] = row.h3.text
    food['url'] = row.a['href']
    food['img'] = row.img['src']
    food['alt_text'] = row.img['alt']
    foods.append(food)

#print(foods)

filename = 'dainik_baskar_news.csv'
with open(filename, 'w', encoding = 'utf-8', errors='ignore', newline='') as f:
    w = csv.DictWriter(f,['title','url','img','alt_text'])
    w.writeheader()
    for food in foods:
        w.writerow(food)

print("Successfully csv file generated")