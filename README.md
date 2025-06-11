# Web Scraping Project

This project is a Python script for scraping store information from a website and formatting it for use with MetaObjects.

---

## 📌 Overview

[`format_for_metaobject.py`](format_for_metaobject.py) is a script that retrieves store information (store name, location, URL) by **prefecture** from a specified website and outputs it as a CSV file.

---

## 📁 File Structure

- [`format_for_metaobject.py`](format_for_metaobject.py) — Main web scraping script
- [`bmc_storelist.csv`](bmc_storelist.csv) — Sample scraped data
- [`.gitignore`](.gitignore) — Specifies files to be ignored by Git
- `README.md` — This file

---

## 📦 Required Libraries

Install the necessary Python packages with pip:

```bash
pip install requests beautifulsoup4 pandas
```

## ▶️ Usage

```
python format_for_metaobject.py
```

After execution, a CSV file named storelist.csv will be generated.

## 📝 Output Format

The generated CSV file will contain the following columns:

- Prefecture
- Store Name
- Location
- URL

## ⚙️ Script Workflow

- Fetches HTML from the specified URL
- Parses the HTML using BeautifulSoup
- Extracts store information from each prefecture section
- Stores the data in a pandas DataFrame and exports it as CSV

⚠️ Notes

- Always check the terms of use of the target website before scraping
- Add appropriate delays between requests if scraping in bulk
- If the structure of the target website changes, you may need to update the script
