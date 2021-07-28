from bs4 import BeautifulSoup
import requests
import urllib.request as ur
import datetime
import urllib
import os
from itertools import count
from collections import OrderedDict
import openpyxl
import re
import pandas as pd


def rednooby_cralwler(input_search):
    url = 'https://news.daum.net/breakingnews/digital'
    post_dict = OrderedDict()

    for pages in count(1):  # 1부터 무한대로 시작(break or return이 나올때까지)
        params = {
            'page': pages,
            'regDate': input_search,
        }
        print(params)
        response = requests.get(url, params=params)
        html = response.text

        # 뷰티풀소프의 인자값 지정
        soup = BeautifulSoup(html, 'lxml')
        pages +=1

        # 쪼개기
        title_list= soup.select('.link_thumb')[:14]
        #print(title_list)

        for tag in title_list:
            if tag['href'] in post_dict:
                return post_dict  # 여기 오게되면 count는 종료됩니다.

            #print(tag.text, tag['href'])
            post_dict[tag['href']] = tag.text
            print(post_dict)

    # return post_dict


if __name__ == "__main__" :
    search_date = input("날짜입력20210101 : ")
    while len(search_date) < 8:
        print("다시 입력하세요")
        search_date = input("정신차리고 다시입력하세요 20210630. : ")

    day_news = rednooby_cralwler(search_date)
