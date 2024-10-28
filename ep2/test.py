import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def view_count(link):
    response = requests.get(link)
    response.encoding = response.apparent_encoding  # 自检测编码
    soup = BeautifulSoup(response.text, "html.parser")
    count = soup.find("span",id="post_view_count").text

    return count

page_url="https://www.cnblogs.com/cate/python"

# 获取编码
response = requests.get(page_url)
response.encoding = response.apparent_encoding  # 自检测编码

#解析html
soup = BeautifulSoup(response.text, "html.parser")

a_tags = soup.find_all("a",class_="post-item-title")

n=1
for a in a_tags:
    link=a["href"]  #链接
    s=view_count(link)
    print(s,n)
    n+=1