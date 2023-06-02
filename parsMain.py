import requests
from bs4 import BeautifulSoup


headers={'User-agent':
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}



url=f'https://shop.kz/catalog/?gclid=CjwKCAjwpayjBhAnEiwA-7ena-z0e4mSwZ5Qm2MbWTQOxt27E1cjaLaL-WVz2Ghd15fT7Jjg16R1kBoCj4IQAvD_BwE%27'
responce=requests.get(url,headers=headers)
list1 =[]


soup=BeautifulSoup(responce.text,'lxml')
data=soup.find('div',class_='bx-content col-xs-12')
data1 = data.find('h2', class_='bx_catalog_tile_title').text
url = 'https://shop.kz/'+data.find('img').get('src')
# print(data1)
# print(url)

data2 = data.find_all('li')
for i in data2:
        list1.append((i.find('h2').text,'https://shop.kz'+i.find('img').get('src')))
# print(list1)

def get():
    return list1