#if you want to scraoe a website:
# 1.Use the API
# 2.Html web scraping using some tool like bs4

# step 0: install all requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url="http://codewithharry.com"

# step 1:Get the HTML
r= requests.get(url)
htmlcontent = r.content
#print(htmlcontent)

# Step 2:parse the HTML
soup=BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify())

# Step 3: Html tree traversal
#Comonly used types of objects
#print(type(title)) #1.Tag
#print(type(title.string)) # 2. Navigablestring
#print(type(soup)) #3.beautifulsoup
# 4. Comment :
#markup="<p><!--this is comment--></p>"
#soup2=BeautifulSoup(markup)
#print(type(soup2.p.string))

#get the title of the html page
title=soup.title

#Get all the paaragraph from the page
paras=soup.find_all('p')
#print(paras)

#get first element in the html page
print(soup.find('p'))

#get classes of any element in the html page
print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p",class_="lead"))

#get the text from  the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#Get all the anchor tags from the page
anchors=soup.find_all('a')
all_links=set()
#Get all the links on the page:
for link in anchors:
    if(link.get('href')!='#'):
        linktext="http://codewithharry.com" +link.get('href')
        all_links.add(link)
        print(linktext)
#print(anchors)

# .contents : A tag's children area available as a list
# .children : A tag's children are available as a generator
navbarsupportedcontent= soup.find(id="nav-content")
for elem in navbarsupportedcontent.children:
    print(elem)

#for item in navbarsupportedcontent.strings:
#   print(item)

#for item in navbarsupportedcontent.stripped_strings:
#   print(item)

#print(navbarsupportedcontent.parent) # to print parent of any element we use .parent
#for item in navbarsupportedcontent.parents:
 #   print(item.name)

#print(navbarsupportedcontent.next_sibling.next_sibling)
#print(navbarsupportedcontent.previous_sibling.previous_sibling)

elem=soup.select('.modal-footer')
print(elem)