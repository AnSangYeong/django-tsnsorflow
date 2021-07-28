from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from itertools import count
import os

def scrape_it_news(date_input):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    url = 'https://news.daum.net/breakingnews/digital?page={}&regDate=' + date_input

    dates = []; links = []; titles = []; contents = []
    for page in count(0,1):
        page +=1

        print()
        print()
        print(f'ㅡㅡㅡㅡㅡ page : {page} 페이지 시작 ㅡㅡㅡㅡㅡ')
        print()
        res = requests.get(url.format(page), headers=headers)
        html = bs(res.text, 'html.parser')
        cont = html.find('ul', {'class': 'list_news2 list_allnews'})
        items = cont.find_all('li')

        for item in items:
            tit = item.find('strong', {'class':'tit_thumb'}).a
            title = tit.get_text()
            link = tit['href']
            content = item.find('span', attrs={'class':'link_txt'}).text.strip()
            print(title)
            if link not in links:
                date = link[21:29]
                dates.append(date)
                links.append(link)
                titles.append(title)
                contents.append(content)
                result = {'기사일자':dates, '링크': links, '기사제목': titles, '기사요약':contents}

            else:
                print()
                print("*********** 마지막 페이지 ***********")
                print()
                return result


if __name__ == "__main__" :
    search_date = input("날짜입력20210101 : ")
    while len(search_date) < 8:
        print("다시 입력하세요")
        search_date = input("정신차리고 다시입력하세요 20210630. : ")
    daily_news = scrape_it_news(search_date)
    df = pd.DataFrame(daily_news)
    print(df)

    filepath = os.path.join(os.getcwd(), "dailynews", "daum_news_list_to_excel_pd_{}.xlsx".format(search_date))
    df.to_excel(filepath)