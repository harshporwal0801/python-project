

import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.facebook.com/"
r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

news=[]
#table = soup.find('div', attrs = {'view-content'}) 

for row in soup.findAll('div',
                         attrs = {'class':'l7ghb35v kjdc1dyq kmwttqpk gh25dzvf jikcssrz n3t5jt4f'}):
    newss = {}
    newss['title'] = row.h2.text
    newss['url'] = row.a['href']
    newss['description'] = row.p.text
    newss['img'] = row.img['src']
    # food['rating'] = row._3LWZlK
    news.append(newss)
print(news)

    

# filename = 'indiatoday.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['title','url','description','img'])
#     w.writeheader()
#     for newss in news:
#         w.writerow(newss)


#print("Successfully csv file generated")