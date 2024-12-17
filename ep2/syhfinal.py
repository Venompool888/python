import requests
from bs4 import BeautifulSoup
import pandas as pd
import myRequests

url = "https://www.kylc.com/stats/global/yearly/g_gdp/2023.html"
response = myRequests.get(url)
response.encoding = 'utf-8'  # 设置编码
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "table"})
rows = table.find("tbody").find_all("tr")

data = []
for row in rows:
    if "tr_region" not in row.get("class", []):
        cols = row.find_all("td")
        if len(cols) >= 5:
            rank = cols[0].get_text(strip=True)
            country = cols[1].get_text(strip=True)
            continent = cols[2].get_text(strip=True)
            gdp_raw = cols[3].get_text(strip=True)
            world_ratio = cols[4].get_text(strip=True)
            data.append([rank, country, continent, gdp_raw, world_ratio])

df = pd.DataFrame(data, columns=["排名", "国家或地区", "所在州", "GDP(原始)", "占世界比率"])

def extract_gdp(value):
    try:
        gdp_value = value.split("(")[-1].split(")")[0]
        gdp_value = float(gdp_value.replace(",", "").strip())
        return gdp_value
    except:
        return None

df["GDP"] = df["GDP(原始)"].apply(extract_gdp)

def clean_country_name(country_name):
    return ''.join([char for char in country_name if not char.isdigit()]).strip()

df["国家或地区"] = df["国家或地区"].apply(clean_country_name)

df_cleaned = df[df["排名"].str.isdigit()].copy()

global_gdp = df_cleaned["GDP"].sum()

print("清洗后的数据（部分）：")
print(df_cleaned)
print(f"\n全球 GDP 总量（清洗后）：{global_gdp:.2f}")

continent_stats = df_cleaned.groupby("所在州").agg(
    GDP总量=("GDP", "sum"),
)
continent_stats["占世界比重(%)"] = (continent_stats["GDP总量"] / global_gdp) * 100

print("\n按洲统计结果：")
print(continent_stats)
df_cleaned.to_csv("gdp_2023_cleaned.csv", index=False, encoding="utf-8-sig")