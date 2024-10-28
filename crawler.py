import requests
from bs4 import BeautifulSoup

url = "https://halo.rin.cool/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')  # 假设文章标题在 <h2> 标签中
    for title in titles:
        print(title.get_text())
else:
    print("请求失败，状态码:", response.status_code)
