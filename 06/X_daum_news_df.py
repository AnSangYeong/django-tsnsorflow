from bs4 import  BeautifulSoup
import datetime
import urllib.request
from urllib.parse import quote
import pandas as pd

now = datetime.datetime.today()
date = str(now.date()).replace("-", "")


def get_news(query, page_num=10):

    news_df = pd.DataFrame(columns=("Title", "Link", "Press", "Datetime", "Article"))
    idx = 0

    url_query = quote(query)
    url = "https://news.daum.net/breakingnews/digital?regDate=" + url_query

    for _ in range(0, page_num):

        search_url = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(search_url, "html.parser")
        links = soup.find_all("div", {"class" : "cont_thumb"})

        for link in links:
            press = link.find("span", {"class" : "info_news"}).get_text()[0:-8]
            news_url = link.find("a").get("href")

            if (news_url == '#'):
                continue
            else:
                news_link = urllib.request.urlopen(news_url).read()
                news_html = BeautifulSoup(news_link, "html.parser")

                try:
                    title = news_html.find("h3", {"class" : "tit_view"}).get_text()
                    datetime = news_html.find("span", {"class" : "txt_info"}).get_text()
                    article = news_html.find("p", {"dmcf-pid" : "k9zHYGg6h2"}).get_text()
                    article = article.replace("\n","")
                    article = article.replace("\t","")
                except:
                    continue

                news_df.loc[idx] = [title, news_url, press, datetime, article]
                idx += 1
                print("#", end="")
    return news_df

query = input('몇일자검색 예시 19801231: ')
news_df = get_news(query, 1)
print('Done')

#news_df