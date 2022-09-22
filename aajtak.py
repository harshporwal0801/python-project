import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.indiatoday.in/aajtak-livetv"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

foods=[]
#table = soup.find('div', attrs = {'class':'may-be-suggest-container'}) 
   
for row in soup.findAll('li',
                         attrs = {'class':'may-we-suggest'}):
    food = {}
    #food['title'] = row.h3.text
    food['Description'] = row.p.text  
    #food['icon']= row.i
    food['url'] = row.a['href']
    food['img'] = row.img['src']
    #food['alt_text'] = row.img['alt']
    #food['location'] = row.li.text
    #food['time'] = row.li.last.text
    foods.append(food)

    
    

filename = 'aajtak.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Description','url','img'])
    w.writeheader()
    for food in foods:
        w.writerow(food)

print("Successfully csv file generated")