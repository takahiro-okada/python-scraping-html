import requests
from bs4 import BeautifulSoup
import pandas as pd

# 対象URL
url = "https://hogehoge/"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

# 結果格納用リスト
rows = []

# 各都道府県のセクションを取得
sections = soup.find_all("section")

for section in sections:
    # 見出しから都道府県名を取得
    h2 = section.find("h2")
    if h2 is None:
        continue
    prefecture_jp = h2.find("span").text.strip()
    
    # テーブル行を取得
    trs = section.find_all("tr")
    for tr in trs:
        th = tr.find("th")
        td = tr.find("td")
        if th and td:
            shop_name = th.text.strip()
            address = td.contents[0].strip()
            a_tag = td.find("a")
            url = a_tag['href'] if a_tag else ""
            rows.append([prefecture_jp, shop_name, address, url])

# CSVとして保存
df = pd.DataFrame(rows, columns=["都道府県", "店名", "場所", "URL"])
df.to_csv("storelist.csv", index=False, encoding="utf-8-sig")

print("✅ CSVファイルを作成しました（storelist.csv）")
