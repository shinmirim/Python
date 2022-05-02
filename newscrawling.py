from urllib import response
from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl


keyword=input("검색할키워드를 입력해주세요:")
kekword=keyword.replace(" ","+")
page=int(input("크롤링할 페이지를 입력해주세요 EX)1(숫자만 입력):"))
print("크롤링할 페이지:"+str(page))
real_page = ((page-1)*10+1)
url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query='+keyword+'&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=80&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start='+str(real_page)
#url="https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+keyword


response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

file=open("news.html","w",encoding="UTF-8")
file.write(response.text)
file.close()

results =soup.findAll("a","news_tit")

print("\t","번호\t","제목")
for i, result in enumerate(results):
    print(i,"\t",i+real_page,"\t",result.get_text())

wb = openpyxl.Workbook()
ws = wb.worksheets[0]
ws.title="news"

filename= "test.xlsx"
wb.save(filename)