from urllib.parse import quote #URL 구문을 분석하기 위한 함수
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#Exel 작업
workbook = xlsxwriter.Workbook('naver news.xlsx')
worksheet = workbook.add_worksheet()
#엑셀 윗줄 작성
worksheet.write(0,0,"No")
worksheet.write(0,1,"뉴스제목")
worksheet.write(0,0,"뉴스내용")


def parse():
    #변수 선언
    global count
    count = 0
    #URL 셋팅
    baseurl = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
    search_keyword = "미세먼지"
    c_url = baseurl + quote(search_keyword) #quote는 특수문자를 문자열로 반환해준다.
    #HTML 불러오기
    response = requests.get(c_url)
    #print(f"status code = {response.status_code}")#HTML 코드 반환
    soup = BeautifulSoup(response.text) #텍스트 파일들로만 정제
    all_news_box = soup.find("ul",{"class":"type01"})
    news_box_list = all_news_box.find_all("li")
    #엑셀에 뉴스 내용 집어넣기
    for one_news in news_box_list:
        if one_news.find("dt") == None:
            continue
        news_title = one_news.find("dt").text
        print(news_title)
        news_content = one_news.find_all("dd")[1].text
        print(news_content)
        print("\n\n")

        count =count + 1
        worksheet.write(count,0,str(count))
        worksheet.write(count,1,news_title)
        worksheet.write(count,2,news_content)
    workbook.close()

parse() #함수 호출
