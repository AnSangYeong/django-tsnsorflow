from bs4 import BeautifulSoup
import requests
import datetime
import re
import pandas as pd

now = datetime.datetime.today()
date = str(now.date()).replace("-", "")

def create_soup(url):

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link, press, ptime):
    print("{}. {}. {}. {} ".format(index+1, title, press, ptime))
    print("  {}".format(link))

def scrape_it_news():
    print("[IT뉴스]")

    url = "https://news.daum.net/breakingnews/digital?page=1&regDate=" + date
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"class":"cont_thumb"})[:15]
    for index, news in enumerate(news_list):
        m_idx = 0
        img = news.find("img")
        if img:
            m_idx = 1

        title = news.find_all("a")[m_idx].get_text().strip()
        link = news.find_all("a")[m_idx]["href"]
        press = news.find_all("span", attrs={"class":"info_news"})[m_idx].get_text()[0:-8].strip()
        ptime = news.find_all("span", attrs={"class":"info_time"})[m_idx].get_text().strip()
        link_txt = news.find_all("span", attrs={"class":"link_txt"})[m_idx].get_text().strip()
        print_news(index, title, link, press, ptime)
        # try:
        #     soup2 = BeautifulSoup(link, "lxml")
        #     articles = soup2.find.all("p", attrs={"dmcf-pid"}).get_text()
        #     for article in articles:
        #         article.find_all('p').get_text()
        # except:
        #     pass

    news.loc = [title, press, ptime, link_txt, link]
    print()




if __name__ == "__main__" :
    scrape_it_news()