import requests
from bs4 import BeautifulSoup

search_name = input("검색어를 입력해주세요: ")
search_page = int(input("페이지 범위를 입력해주세요: "))
count = 0
for page in range(1, search_page*10, 10):
    print(page)
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_name}&start={page}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    news_items = soup.find_all("a", "news_tit")
    for news_item in news_items:
        count += 1
        print(news_item.text)
        print(news_item['href'])
print(count)