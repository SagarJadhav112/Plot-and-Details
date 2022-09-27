#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests
from csv import writer

url="https://www.pararius.com/apartments/amsterdam"
page=requests.get(url)
#print(page)
soup=BeautifulSoup(page.content,'html.parser')

lists=soup.find_all('section',class_="listing-search-item")



lists=soup.find_all('section',class_="listing-search-item")

with open ('housing.csv','w',encoding='utf8',newline="") as f:
    thewriter=writer(f)
    header=['Title','Location','Price','Area']
    thewriter.writerow(header)
    for i in lists:
    
        title=i.find('a', class_="listing-search-item__link--title").text.replace('\n','')
        location=i.find('div', class_="listing-search-item__sub-title").text.replace('\n','')
        price=i.find('div', class_="listing-search-item__price").text.replace('\n','')
        area=i.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')
        info=[title,location,price,area]
        thewriter.writerow(info)
        
    
        


# In[ ]:





# In[67]:





# In[ ]:





# In[ ]:





# In[ ]:




