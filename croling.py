import requests
from bs4 import BeautifulSoup


site_url = 'https://www.10000recipe.com/ranking/home_new.html'

raw = requests.get(site_url)

soup = BeautifulSoup(raw.text, 'html.parser')

box = soup.find('ul',{'class':'common_sp_list_ul ea4'})



recipes = box.find_all(attrs = {'class':'common_sp_caption_tit line2'})


i =1
print('맛있는 레시피 랭킹 100등!!')
for recipe in recipes:
    print(i , recipe.text)
    i += 1
        
