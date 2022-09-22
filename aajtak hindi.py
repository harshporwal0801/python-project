from gettext import find
import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.aajtak.in/lifestyle"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

foods=[]
table = soup.find('div', attrs = {'class':'leadStory-style1 bg-yellow top_dharm'}) 
   
for row in table.findAll('div',attrs = {'class':'container'}):
    food = {}
    food['title'] = row.h2.text
    #food['Description'] = row.p.text  
    #food['icon']= row.i
    food['url'] = row.a['href']
    food['img'] = row.img['src']
    food['alt_text'] = row.img['alt']
    #food['location'] = row.li.text
    #food['time'] = row.li.last.text
    foods.append(food)
print(foods)

    
    

filename = 'aajtak_hindi.csv'
with open(filename, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f,['title','Description','url','img','alt_text'])
    w.writeheader()
    for food in foods:
        w.writerow(food)

print("Successfully csv file generated")