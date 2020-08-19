import requests
import lxml.etree
import conn
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import time
from tabulate import tabulate

'''
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,en-GB;q=0.4',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}



def get_page(url):
  try:
    time.sleep(3)
    with requests.session() as s:
      s.headers.update(headers)
      r = s.get(url)
      return r.content.decode('utf-8')

  except Exception as err:
    print(err)
    return ""

def gen_urls():
  urls = dict(BJ='https://www.lagou.com/beijing-zhaopin/Python/'
              , SH='https://www.lagou.com/shanghai-zhaopin/Python/'
              , GZ='https://www.lagou.com/guangzhou-zhaopin/Python/'
              , SZ='https://www.lagou.com/shenzhen-zhaopin/Python/')
  for city in urls.keys():
    url = urls[city]
    for page in range(1, 16):
      yield url+str(page), city
for item in gen_urls():
  print(item)








dic = dict(
  a=1,
  b=2,
  c=3)

for i in dic:
  print(dic[i])

for i in dic.keys():
  print(i)

for i in dic.values():
  print(i)

for i in dic.items():
  print(i)
dic['d'] = 4
print(dic)

del dic['d']
print(dic)
'''

url = r'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=60'



headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,en-GB;q=0.4', 
'Cache-Control': 'no-cache', 
'Connection': 'keep-alive', 
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

response = requests.post(url,headers=headers)


