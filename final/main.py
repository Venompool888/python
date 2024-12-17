import requests
from bs4 import BeautifulSoup
import pandas as pd

# 示例网页的URL
url = "https://www.kylc.com/stats/global/yearly/g_gdp/2023.html"

# 获取网页内容并设置编码
response = requests.get(url)
response.encoding = response.apparent_encoding  # 自检测编码

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 提取所有<tr>标签，并排除广告内容
tr_tags = soup.find_all('tr')
filtered_tr = [
    tr for tr in tr_tags
    if not (
        (tr.find('td', colspan=True) and tr.find('ins', class_="adsbygoogle")) or
        (tr.find('td') and "欧盟地区" in tr.text)  # 排除包含“欧盟地区”的<tr>
    )
]

# 存储提取的数据
data = []

# 遍历过滤后的<tr>标签
for tr in filtered_tr:
    # 提取<td>内容
    td_tags = tr.find_all('td')
    td_texts = [td.text.strip() for td in td_tags]

    # 确保行数据足够长
    if len(td_texts) >= 5:
        rank = td_texts[0]  # 排名
        country_or_region = td_texts[1]  # 国家或地区
        continent = td_texts[2]          # 所在州
        gdp = td_texts[3]                # GDP
        share = td_texts[4]              # 占世界比率

        # 处理GDP值，提取括号内数据并转换为数值
        if '(' in gdp:
            gdp_numeric = int(gdp.split('(')[1].strip(')').replace(',', '').strip())
        else:
            gdp_numeric = None

        # 添加到数据列表
        data.append([country_or_region, continent, gdp, gdp_numeric, share])

# 转换为DataFrame
columns = ["国家或地区", "所在州", "GDP", "GDP数值", "占世界比率"]
df = pd.DataFrame(data, columns=columns)

# 清洗数据：去除“非国家”数据（如“全世界”）
df_cleaned = df[~df["国家或地区"].str.contains("全世界|World", na=False)]

# 计算全球GDP总量
global_gdp_total = df_cleaned["GDP数值"].sum()

# 输出清洗后的数据和全球GDP总量
print("\n清洗后的数据（部分）：")
print(df_cleaned.head()) 
print(f"\n全球GDP总量：{global_gdp_total}")

# 按洲统计GDP总量和占比
continent_stats = df_cleaned.groupby("所在州").agg(
    GDP总量=("GDP数值", "sum"),
    国家数量=("国家或地区", "count")
)
continent_stats["占世界比率"] = (continent_stats["GDP总量"] / global_gdp_total) * 100

# 输出按洲统计结果
print("\n按洲统计GDP总量及占比：")
print(continent_stats)

# 保存结果为CSV
df_cleaned.to_csv("gdp_2023_cleaned.csv", index=False, encoding="utf-8-sig")
continent_stats.to_csv("gdp_2023_continent_stats.csv", index=True, encoding="utf-8-sig")
print("\n数据已保存到 gdp_2023_cleaned.csv 和 gdp_2023_continent_stats.csv")
