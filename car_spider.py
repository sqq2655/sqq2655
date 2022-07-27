import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def spider(page_id):
    url = "https://www.autohome.com.cn/all/"+str(page_id)+"/#liststarts"
    response = requests.get(url=url)
    response.encoding="GBK"

    soup_obj = BeautifulSoup(response.text,'html.parser')
    content = soup_obj.find(name="div",attrs={"id":"auto-channel-lazyload-article"})
    li_list = content.findAll(name="li")
    for i in li_list:
        exist = i.find(name="h3")
        if not exist: continue
        title = i.find(name="h3").text
        summary = i.find(name="p").text
        a = "https:"+i.find(name="a").get("href")
        img = "https:"+i.find(name="img").get("src")
        tags = a.split("/",4)[3]
        print(response.url,title,tags)
    return response.text





if __name__ == '__main__':
    t = ThreadPoolExecutor(8)
    for page_id in range(1,9936):
        t.submit(spider,page_id)
    t.shutdown()