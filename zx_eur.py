# -*- coding: UTF-8 -*-
"""
 获取众信旅游
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# 获得指定开始排行
def get_url(root_url,start):
    return root_url+str(start)+"/0/0/s1/"

def get_review(page_url):
    paths_list=[]
    response=requests.get(page_url)
    soup=BeautifulSoup(response.text,"lxml")
    soup=soup.find('div','main_left')
    for tag_li in soup.find_all('div','main_left1'):
        dict={}
        if(tag_li.find('span')):
            dict['path']=tag_li.find('span').string
        if(tag_li.find('div','price').find('b')):
            dict['price']=tag_li.find('div','price').find('b').string
        if(tag_li.find('div','place_departure').find('span','red')):
            dict['place']=tag_li.find('div','place_departure').find('span','red').string
        if(tag_li.find('div','departure_date').find('span')):
            dict['date']=tag_li.find('div','departure_date').find('span').string
        paths_list.append(dict)
    return paths_list

if __name__ == "__main__":
    root_url="https://search.uzai.com/ouzhou/"
    start=1
    while(start<3):
        paths_list=get_review(get_url(root_url,start))
        for path_dict in paths_list:
            print('Europe path:'+path_dict.get('path'))
            print('Europe price:'+path_dict.get('price'))
            print('Europe place:'+path_dict.get('place'))
            print('Europe date:'+path_dict.get('date'))
            print('------------------------------------------------------')
        start+=1

