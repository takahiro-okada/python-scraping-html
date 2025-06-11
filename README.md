# Web Scraping Project

このプロジェクトは、Web サイトから店舗情報をスクレイピングして、メタオブジェクト用にフォーマットするための Python スクリプトです。

## 概要

[`format_for_metaobject.py`](format_for_metaobject.py)は、指定された Web サイトから都道府県別の店舗情報（店名、場所、URL）を取得し、CSV ファイルとして出力するスクリプトです。

## ファイル構成

- [`format_for_metaobject.py`](format_for_metaobject.py) - メインのスクレイピングスクリプト
- [`bmc_storelist.csv`](bmc_storelist.csv) - スクレイピング結果のサンプルデータ
- [`.gitignore`](.gitignore) - Git で管理しないファイルの設定
- `README.md` - このファイル

## 必要なライブラリ

```bash
pip install requests beautifulsoup4 pandas
```

## 使用方法

1. スクリプトを実行：

```bash
python format_for_metaobject.py
```

2. 実行後、`storelist.csv`ファイルが生成されます

## 出力形式

CSV ファイルには以下のカラムが含まれます：

- 都道府県
- 店名
- 場所
- URL

## スクリプトの動作

1. 指定された URL から HTML を取得
2. BeautifulSoup を使って HTML を解析
3. 各都道府県のセクションから店舗情報を抽出
4. pandas DataFrame に格納して CSV として出力

## 注意事項

- スクレイピング対象の Web サイトの利用規約を確認してください
- 大量のリクエストを送信する場合は、適切な間隔を設けてください
- 対象サイトの構造が変更された場合、スクリプトの修正が必要になる可能性があります

## ライセンス

このプロジェクトは個人利用を想定しています。商用利用する場合は、対象サイトの利用規約を確認してください。
