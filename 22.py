import gzip
import json
import re


def load_article_text():
    with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
        for line in f:
            article = json.loads(line)
            if article["title"] == "イギリス":
                return article["text"]


matches = re.findall(r"\[\[Category:(.+?)(?:\|.*)?\]\]", load_article_text())

for match in matches:
    print(match)
'''
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国
1801年に設立された州・地域
'''
