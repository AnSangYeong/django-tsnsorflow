import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs
os.chdir(r'C:\Users\An-SangYeong\___\111 do-it-python-master\test')


'''
url='https://news.daum.net/breakingnews/digital?page=1'
# 마법의 명령어
soup = bs(ur.urlopen(url).read(),'html.parser')

f= open('links.txt','w')
for i in soup.find_all('div',{"class":"cont_thumb"}):
    print(i.find_all('a')[0].get('href'))
    f.write(i.find_all('a')[0].get('href')+'\n' )
f.close()
'''




url='https://news.daum.net/breakingnews/digital?page=1'     # 기사 목록모으기
soup=bs(ur.urlopen(url).read(),'lxml')                      # 기사 목록 객체로 열기
article1 ='https://news.v.daum.net/v/20200427090630709'     # 특정기사 본문 url
soup2 = bs(ur.urlopen(article1).read(),'lxml')              # soup2 객체로 열기


f= open('article_total.txt','w', encoding="utf-8-sig", newline="\n")
for i in soup.find_all('div', {"class" : "cont_thumb"}):
    try:                                                    # 여기서 try로 예외를 지정해주는 이유는 각 명령어를 실행하다가 혹시 그 어떤 곳에서 중단되더라도 마지막까지 실행되도록 하기 위해서입니다.
        f.write(i.text+'\n')                        # 제목을 추출하는 명령어입니다. '\n'를 붙이는 이유는 제목이 끝난 후 한 줄을 띄워주기 위해서입니다. 이하 동일합니다
        f.write(i.find_all('a')[0].get('href'))             # 각 영역(div) 안에서 'a' 태그를 추출해내고, 그 안에서 하이퍼링크('href') 주소를 얻어냅니다. 그것을 바로 파일로 저장하고, 한 칸 띄워줍니다.
        soup2=bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'lxml') # 위에서 얻어낸 하이퍼링크 주소로 곧바로 뷰티풀소프 객체로 다시 저장합니다.
        for j in soup2.find_all('p'):                       # 다시 문단만 추출해냅니다. 기사 본문을 모을 수 있습니다.
            f.write(j.text+'\n')                            # 추출한 문단을 파일로 저장합니다.
    except:
        pass                                                # try문을 쓰면 별 다른 예외처리를 하지 않더라도 except 구문을 써야 합니다.
f.close()
