import requests
import shutil
import json
import re
import os

url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1614319565639&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160'
dirt = ''

proxies = {'http': 'http://127.0.0.1:7890' , 'https': 'http://127.0.0.1:7890'}

def down_img(url):
    response = requests.get(url,proxies=proxies).text
    r = json.loads(response)['images'][0]
    url = re.findall('(.*?)&',r['url'])[0]
    name = r['copyright'].replace('/','-')
    print(url)
    print(name)
    url = 'https://cn.bing.com'+url
    response = requests.get(url)
    data = response.content
    with open(dirt+name+'.jpg','wb') as f:
        f.write(data)

def move_img(url):
    filelist = os.listdir(dirt)
    for i in filelist:
        j = os.path.join(dirt,i)
        if len(filelist) == 1 or os.path.isfile(j):
            response = requests.get(url,proxies=proxies).text
            r = json.loads(response)['images'][0]
            name = r['copyright'].replace('/','-')
            if i[:-4] != name:
                shutil.move(j, dirt+'history')
                return 1
            
def save_img():
    if move_img(url):
        down_img(url)


