import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.indiatoday.in/india"
r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

news=[]
table = soup.find('div', attrs = {'view-content'}) 

for row in table.findAll('div',
                         attrs = {'class':'catagory-listing'}):
    newss = {}
    newss['title'] = row.h2.text
    newss['url'] = row.a['href']
    newss['description'] = row.p.text
    newss['img'] = row.img['src']
    # food['rating'] = row._3LWZlK
    news.append(newss)

    

filename = 'indiatoday.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','url','description','img'])
    w.writeheader()
    for newss in news:
        w.writerow(newss)


print("Successfully csv file generated")