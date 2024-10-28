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

def extract_article_content(article_url, save_directory, title, author, time, yuedu_number):
    """
    提取给定文章链接的内容并保存到指定目录的文本文件中。

    :param article_url: 文章链接
    :param save_directory: 保存目录路径
    :param title: 文章标题
    :param author: 文章作者
    :param time: 文章发布时间
    :param yuedu_number: 阅读数量
    """
    # 获取页面内容
    page_url="https://www.cnblogs.com/cate/python"
    response = requests.get(article_url)
    response.encoding = response.apparent_encoding  # 自检测编码

    # 解析 HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 提取文章内容
    article_content = []

    # 获取所有的元素，包括标题、段落和 pre 标签
    for element in soup.find_all(['h2', 'h3', 'p', 'pre']):
        # 只添加有内容的元素
        if element.get_text(strip=True):
            article_content.append(element.get_text(strip=True))

    # 确保保存目录存在
    os.makedirs(save_directory, exist_ok=True)

    # 创建文件名
    file_name = os.path.join(save_directory, f"{title}.txt")

    # 将提取的内容写入文本文件
    with open(file_name, "w", encoding="utf-8") as file:
        # 写入标题、作者、时间和阅读数量
        file.write(f"标题: {title}\n")
        file.write(f"作者: {author}\n")
        file.write(f"发布时间: {time}\n")
        file.write(f"阅读数量: {yuedu_number}\n")
        file.write("\n")  # 空行分隔

        # 写入文章内容
        for line in article_content:
            file.write(line + "\n")

    print(f"文章内容已成功提取并保存到 {file_name}")



# 获取脚本所在目录
page_url="https://www.cnblogs.com/cate/python"

script_dir = os.path.dirname(os.path.abspath(__file__))

obj_dir = os.path.join(script_dir, "project")

# 创建这个新闻的文件夹
folder_path = os.path.join(obj_dir)
os.makedirs(folder_path)

# 获取编码
response = requests.get(page_url)
response.encoding = response.apparent_encoding  # 自检测编码

#解析html
soup = BeautifulSoup(response.text, "html.parser")

#获取新闻链接、标题、时间
a_tags = soup.find_all("a",class_="post-item-title")
span_tags = soup.find_all("span",class_="post-meta-item")
author_tags = soup.find_all("a",class_="post-item-author")

    
n=1
for a in a_tags:
    author=author_tags[n-1].text #作者
    title=a.text    #标题
    link=a["href"]  #链接
    time=span_tags[n-1].text    #时间
    count=view_count(link) #阅读数


    extract_article_content(link, folder_path, title, author, time, count)


    n+=1


