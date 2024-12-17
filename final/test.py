import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 目标链接
page_url="https://www.kylc.com/stats/global/yearly/g_gdp/2023.html"



# 获取编码
response = requests.get(page_url)
response.encoding = response.apparent_encoding  # 自检测编码

#解析html
soup = BeautifulSoup(response.text, "html.parser")

# 提取所有<tr>标签，排除广告内容
tr_tag = soup.find_all('tr')
filtered_tr = [
    tr for tr in tr_tag
    if not (tr.find('td', colspan=True) and tr.find('ins', class_="adsbygoogle"))
]

# 输出过滤后的<tr>标签
for tr_index, tr in enumerate(filtered_tr):
    print(f"处理第 {tr_index + 1} 个 <tr> 标签内容:")
    print(tr)
    print("-" * 40)