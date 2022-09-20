import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.indiatoday.in/india/video/opposition-alleges-mann-deplaned-aap-terms-charges-as-propaganda-2002352-2022-09-20"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

foods=[]
#table = soup.find('div', attrs = {'class':'row'}) 
   
for row in soup.findAll('div',
                         attrs = {'id':'trending-videos'}):
    food = {}
    #food['title'] = row.h3.text
    food['title'] = row.p.text
    #food['icon']= row.i
    food['url'] = row.a['href']
    #food['img'] = row.img['src']
    #food['alt_text'] = row.img['alt']
    # food['location'] = row.li.text
    #food['time'] = row.li.last.text
    foods.append(food)
print(foods)
    
    

# filename = 'the_pioneer_news.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['title','description','url','img','alt_text'])
#     w.writeheader()
#     for food in foods:
#         w.writerow(food)

# print("Successfully csv file generated")