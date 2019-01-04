result = 10
print(result)
result = 20
print(result)

hello = "world"
world = "hello"

print(hello)
print(world)

password = 1234

if password == 1234:
    print("문을 열어줍니다.")
else:
    print("아무것도 하지 않습니다.")

password = 1235

score = 86

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print("F")

score = 77

def print_hello():
    print("hello")

print_hello()

def pikachu():
    print("전기공격")

pikachu()

def print_message(p_message):
    print(p_message)

print_message("bye")


def pikachu(skill_number):
    if skill_number == 1:
        print("전기공격")
    elif skill_number ==2:
        print("몸통박치기")

pikachu(1)

def plus(val1,val2):
    return val1 + val2

plus(10,20)

result_return = plus(10,20)
print("result_return",result_return)


def print_hello(p1, p2):
    print("using print:", p1+p2)

def plus(val1, val2):
    return val1 + val2

result = print_hello(10,20)
result_return = plus(10,20)

print("result:",result)
print("result_return", result_return)

def plus(val1,val2):
    return val1+val2

def sub(val1,val2):
    return val1-val2

def mul(val1,val2):
    return val1*val2

def div(val1, val2):
    return val1 / val2

result_plus = plus(10,20)
result_plus2 = plus(20,30)
result_plus3 = plus(40,40)

print(result_plus,result_plus2,result_plus3)

def f(param1):
    return param1 + 10

def g(param1):
    return param1 * 20

print(f(g(10)))

for item in range(0,10):
    print('hello')

print(list(range(1,10)))

list_number = [0,1,2,2,4]
list_string = ["kyeongrok","yeongduk","jihyun"]

num_list=[0,1,2,2,4]
num_list[3]

for item in [0,1,2,2,4]:
    print(item)

for idx in range(1,10):
    print(2,"x",idx,"=",2*idx)

for num in num_list:
    print(num*2)

#num_lsit 각각에 2를 곱합 결과 
results = [num*2 for num in num_list]

a = 10
b = -20
c = 30
total = a+b+c
print(total)

a = 12.5
b = 35.8
c = 50
total = a+b+c
average = total / 3
print(average)

print(30/4)
print(4/30)
print(5/10)
print(10/5)
print(1/1)
print(type(1))
print(type(1/1))

print(5+4)
print(5.0-3.0)
print(10.5*4)
print(200/10)
print(200 % 10)
print(20/7)
print(20%7)
print(20 // 7)

cheolsu_kor = 88
cheolsu_eng = 76
cheolsu_math = 95
younghee_kor = 100
younghee_eng = 67
younghee_math = 80

cheolsu_average = (cheolsu_kor + cheolsu_eng + cheolsu_math) / 3
younghee_average = (younghee_kor + younghee_eng + younghee_math) /3


if cheolsu_average > younghee_average:
    print("철수가 높아요")
elif cheolsu_average == younghee_average:
    print("둘이 같아요")
else:
    print("영희가 높아요")

crawling = "Data crawling is fun"
parsing = 'data parsing is also fun'

print(crawling)
print(parsing)
print(type(crawling))
print(type(parsing))

print(crawling+ " " + parsing)

r = 10
pie = 3.141592
area = (r ** 2) * pie
print("원의넓이" +str(area))

str(area)

data = crawling[0:4]
crawling[0:13]
crawling[17:]
crawling[19]
n_range= crawling[-1:]
crawling[-2:]
also = parsing[16:16+4]
parsing[0:20]

print(crawling.find('Data'))
print(crawling.find("fun"))
print(parsing.find("Data"))
print(crawling.find('parsing'))
print(parsing.find("crawling"))

str_data = "random:data:choice:sampling:mini-batch:unpooling:training"
split_str_data = str_data.split(":")
print(str_data)
print(split_str_data)

for i in range(0,len(split_str_data)):
    print(split_str_data[i])

crawling = "Data crawling is fun"

print(crawling.replace("search","analyze"))
print(crawling.replace("Data","Web"))

introduction = "Project Gutenberg never charges a fee, for anything. Everything form Project. this project is good withoug cost to readers. free"
print(introduction.count('Project'))

str_data = "{a1 : 20} , {a2:30}, {a3:15}, {a4:50}, {a5:-15},{a6:80},{a7:0},{a8:-110}"

total = 0
split_str_data = str_data.split(",")
for i in range(0,len(split_str_data)):
    str_temp = split_str_data[i].split(":")[1].split("}")[0]
    num_tmp = int(str_temp)
    total += num_tmp


print(total)

name=[]
type(name)
name = ['kyeongrok']

int_list = [1,2,3,4,5]
float_list = [1.1,2.2,3.3,4.4,5.5]
string_list = ["crawling","parsing","data","extract","pre-processing"]
all_list = [int_list, float_list, string_list]


all_list

for i in range(0,len(all_list)):
    print(all_list[i])


int_list = [1,2,3,4,5]

int_list.append(6)
int_list.insert(1,12)

int_list.remove(4)

del int_list[0:2]

int_list = [3,1,5,4,2]
float_list = [4.4, 2.2, 3.3, 5.5, 1.1]
string_list = ["crawling","parsing","data","extract","pre-processing"]

int_list.sort()
float_list.sort(reverse=0)
string_list.sort()

int_list = [1,5,4,3,7,5,4,2,4]
string_list = ["car","cat","can","cut","cat","cnn","cure","cat"]

print(int_list.count(4))
print(string_list.count("cat"))


user = {}
print(user)
print(type(user))

user = {"name":"kyeongrok"}
print(user)

class1 = {0:"kyeongrok",1:"victoria"}
print(class1)
print(class1[0])

naver = {
    "name":"naver",
    "url":"www.naver.com",
    "userid":"nv",
    "passwd":"1234"
}

google = {
    "name": "google",
    "url": "www.naver.com",
    "userid":"gg",
    "passwd":"1234"
}

print(naver)
print(google)
print(type(naver))
print(type(google))

site = {"naver":"www.naver.com", "google":"www.google.com"}
site["naver"]
site["google"]

site["daum"] = "www.daum.net"
print(site)
site["daum"]

site["yahoo"] = "www.yahoo.com"
site["yahoo"]

del site["yahoo"]

insert_key = "yahoo"
if site.get(insert_key) == None :
    print(insert_key+"없어")

site = {
    "naver" : "www.naver.com",
    "google" : "www.google.com",
    "daum" : "www.daum.net"
}

site.values()

for values in site.values():
    print(values)

for item in site.items():
    print(item)


list(site.items())

from urllib.request import urlopen

url = "https://www.naver.com/"
html = urlopen(url)

print(html.read())

import bs4
html_str = "<html><div>hello</div></html>"
bs_obj= bs4.BeautifulSoup(html_str,"html.parser")

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))


html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
print(ul)

bs_obj.find("ul").find("li").text

bs_obj.find("ul").findAll("li")[1].text



html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")

bs_obj.find("ul",{"class":"reply"})

html_str = """
<html>
    <body>
        <ul class="ko">
            <li>
                <a href="https://www.naver.com">네이버</a>
            </li>
            <li>
                <a href="https://www.daum.net">다음</a>
            </li>
        </ul>
        <ul class="sns">
        <li>
                <a href="https://www.google.com">구글</a>
            </li>
            <li>
                <a href="https://www.facebook.com">페이스북</a>
            </li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
atag = bs_obj.find("a")
bs_obj.find("a")['href']

import urllib.request
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

print(bs_obj.head())

top_right = bs_obj.find('div',{"class":"area_links"})
top_right.find('a',{"class":"al_jr"}).text

test = bs_obj.find("a",{"class":"an_a mn_mail"})
test.find("span",{"class":"an_txt"}).text

ul = bs_obj.find('ul',{"class":"an_l"})
lis=ul.findAll("li")
lis[0]

for li in lis:
    a_tag = li.find("a")
    print(a_tag)

txt1=[]
for span in lis:
    txt = span.find("span",{"class":"an_txt"}).text
    print(txt)
    txt1 +=[txt]

txt1

url = "http://news.naver.com/"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html,"html.parser")

print(bs_obj)

newsnow_txarea = bs_obj.find("ul",{"class":"newsnow_txarea"})
lis = newsnow_txarea.findAll("li")

#findAll() 뒤에는 .text 안먹힘!! find()에만 먹힘.

for li in lis:
    strong = li.find("strong").text
    print(strong)


import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io"
result = requests.get(url =url)

bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)

lf_items = bs_obj.findAll("div",{"class":"lf-item"})
print(lf_items)

hrefs = [div.find("a")['href'] for div in lf_items]
print(hrefs)

len(hrefs)
hrefs[0:5]

url = "https://bp.eosgo.io/listing/eos-ai-singapore/"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content,"html.parser")
print(bs_obj)

profile_name = bs_obj.find("div",{"class":"profile-name"})
h1_bp_name = profile_name.find("h1")
bp_name = h1_bp_name.text
print(bp_name)

cover_buttons = bs_obj.find("div",{"class":"buttons medium button-plain"})
location = cover_buttons.find("span",{"class":"button-label"}).text
location

lis= bs_obj.find("div",{"class":"cover-buttons"}).findAll("li")
li_tag=lis[1]

a_tag = li_tag.find("a")
link = a_tag['href']

link


#---- 함수(def)로 묶기 -----

def get_bp_info(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content,"html.parser")

    profile_name = bs_obj.find("div",{"class":"profile-name"})

    h1_bp_name = profile_name.find("h1")
    bp_name = h1_bp_name.text

    cover_buttons = bs_obj.find("div",{"class":"buttons medium button-plain"})
    location = cover_buttons.find("span",{"class":"button-label"}).text


    lis= bs_obj.find("div",{"class":"cover-buttons"}).findAll("li")
    li_tag=lis[1]

    a_tag = li_tag.find("a")
    link = a_tag['href']

    dictionary1 = {}
    dictionary1['name'] = bp_name
    dictionary1['location'] = location
    dictionary1['link'] = link

    return dictionary1

dic_result = get_bp_info(url)
print(dic_result)

get_bp_info("https://bp.eosgo.io/listing/eos-beijing/")

for number in range(0,5):
    dic_result= get_bp_info(hrefs[number])
    print(dic_result)

import requests
from bs4 import BeautifulSoup

url = "http://jolse.com/category/tonermist/43/?page=1"
result = requests.get(url =url)

bs_obj = BeautifulSoup(result.content,"html.parser")

ul = bs_obj.find("ul",{"class":"prdList column5"})
boxes = ul.findAll("div",{"class":"box"})

for box in boxes:
    ptag = box.find("p",{"class":"name"})
    span = ptag.findAll("span")
    print(span[1].text)

def get_proudct_info(box):
    ptag = box.find("p",{"class":"name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")
    
    name = spans_name[1].text
    price = spans_price[1].text

    atag = box.find("a")
    link = atag['href']

    return {"name":name , "price":price, "link":link}


def get_page_products(url):
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content,"html.parser")
    ul = bs_obj.find("ul",{"class":"prdList column5"})

    boxes = ul.findAll("div", {"class":"box"})
    product_info_list = [get_proudct_info(box) for box in boxes]

    return product_info_list

url = "http://jolse.com/category/tonermist/43/?page=1"
page_products = get_page_products(url)
print(page_products)


urls = [ "http://jolse.com/category/tonermist/43/?page=1",
"http://jolse.com/category/tonermist/43/?page=2",
"http://jolse.com/category/tonermist/43/?page=3",
"http://jolse.com/category/tonermist/43/?page=4",
"http://jolse.com/category/tonermist/43/?page=5",
]

page_products = get_page_products(urls[0])
print(page_products)

for page_number in range(0,5):
    page_products = get_page_products(urls[page_number])
    print(page_products)


import json
json_str = '[{"name":"kyeongrok", "age":"32"},{"name":"bomi","age":"25"}]'
json_obj = json.loads(json_str)

print(json_obj)
json_obj[:2]

json_obj[0]['name']
json_obj[1]['age']

for student in json_obj:
    print(student['age'],student['name'])

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "9hKI9LYletZ6ghtGHxuO"
client_secret = "GKK4aB9Pzb"
encText = urllib.parse.quote("강남역")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


import requests
from urllib.parse import urlparse

keyword="강남역"
url = "https://openapi.naver.com/v1/search/blog?query="+ keyword + "&display=100"
result = requests.get(urlparse(url).geturl(),headers={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret})

json_obj=result.json()
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['display'])


json_obj = {"name":"kyeongrok","age":"32","where":"역삼동","phone_number":"010-3588-0000",
"friends":[{"name":"sian","age":"32"},{"name":"kyuri","age":"24"}]
}
print(json_obj["friends"])

import requests
from urllib.parse import urlparse

def get_api_result(keyword, display,start):
    url = "https://openapi.naver.com/v1/search/blog?query="+ keyword + "&display=" + str(display) + "&start" + str(start)
    result = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret})
    return result.json()

keyword = "강남역"
json_obj = get_api_result(keyword,100,101)

for item in json_obj['items']:
    item


def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100 ,page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>","").replace("</b>","")
        print(title+"@"+item['bloggername']+"@"+item['link'])

call_and_print(keyword,1)
call_and_print(keyword,101)
call_and_print(keyword,201)
call_and_print(keyword,301)
call_and_print(keyword,401)

from urllib.request import urlopen
import json

url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2019-01-03"
text = urlopen(url)

from_date = "2010-01-01"
to_date = "2019-01-03"
url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/"+from_date + "/edate/" + to_date
text = urlopen(url)

print(text.read())


html = urlopen(url)
json_obj = json.load(html)
print(json_obj[0:10])

for item in json_obj:
    print(item['date']+"@"+item['settlement'])



import requests
import bs4

endpoint = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
serviceKey = "nKVjJPmJBURFDR2mLxZoVR4wEtrYvl0LKhIAINuIPmMEUlfGOKG23XOIKh9KXxDC9KdxQ1b9BkQKVM01yJexhQ%3D%3D"
numOfRows="10"
pageSize = "1"
pageNo = "1"
MobileOs = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "15"
areaCode = "1"
sigunguCode = "4"
listYN = "Y"

paramset = "serviceKey=" + serviceKey + "&" + "numOfRows="+ numOfRows + "&" +"pageSize="+ pageSize +"&" +"pageNo=" + pageNo + "&"+ "MobileOS="+MobileOs + "&"+ "MobileApp="+ MobileApp + "&"+"arrange=" + arrange + "&" + "contentTypeId="+ contentTypeId + "&" + "areaCode="+areaCode + "&"+"sigunguCode="+sigunguCode + "&" + "listYN=" + listYN
url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
print(bs_obj.findAll("title"))


from urllib.parse import quote
quote("서울특별시")

from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "nKVjJPmJBURFDR2mLxZoVR4wEtrYvl0LKhIAINuIPmMEUlfGOKG23XOIKh9KXxDC9KdxQ1b9BkQKVM01yJexhQ%3D%3D"

Q0 = quote("서울특별시")
Q1 = quote("강남구")
QT = "1"
QN = quote("삼성약국")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "5000"
pageSize = "10"

paramset = "serviceKey=" + serviceKey +"&" + "Q0=" + Q0 + "&"+"ORD="+ORD + "&"+"pageNo="+pageNo + "&"+"startPage="+startPage +"&"+"numOfRows="+numOfRows

url = endpoint + paramset
print("url:"+url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")


count=0

for item in items:
    tagged_item = item.find("dutytime1c")
    if (tagged_item != None):
        close_time = int(tagged_item.text)
        if (close_time > 2100) :
            count += 1

print("월요일 9시 이후 하는 약국 수:"+str(count))


