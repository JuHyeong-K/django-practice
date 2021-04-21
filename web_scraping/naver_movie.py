import requests
from bs4 import BeautifulSoup
# import re

# url = "https://movie.naver.com/movie/running/current.nhn"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# movie_titles = soup.select('dt.tit > a')
# movie_data = []
# for movie_title in movie_titles:
#     # code = re.findall('\d+', movie_title['href'])[0] # 돼지 잡는 칼로 야채 써는 격
#     code = movie_title['href'].split('?code=')[1]
#     temp_data = {
#         "title" : movie_title.text,
#         "code": code
#         }
#     movie_data.append(temp_data)

def get_movie_title_code():
    url = "https://movie.naver.com/movie/running/current.nhn"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_titles = soup.select('dt.tit > a')
    movie_data = []
    for movie_title in movie_titles:
        # code = re.findall('\d+', movie_title['href'])[0] # 돼지 잡는 칼로 야채 써는 격
        code = movie_title['href'].split('?code=')[1]
        temp_data = {
            "title" : movie_title.text,
            "code": code
            }
        movie_data.append(temp_data)
    return movie_data

movie_data = get_movie_title_code()

for i, movie in enumerate(movie_data):
    reviews = {
    'comments': [],
    'comments_score': []
    }
    for index in range(1):
        code = movie['code']
        headers = {
            'authority': 'movie.naver.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'iframe',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'referer': 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189075&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'NNB=YTCBYGMUQUEWA; NaverSuggestUse=use%26unuse; NRTK=ag#20s_gr#0_ma#-2_si#0_en#-2_sp#-1; NDARK=N; _ga=GA1.2.1348994037.1614128644; _fbp=fb.1.1614128644438.366270856; nid_inf=582830848; NID_AUT=hY1X3Qk08uR9PDC14aeJkrIcopkcM8VrKbtfjx6bvi1rYkgTCXbYIOzrhokFGRuP; NID_JKL=JsQBMvSsYARB0flcBSd6kMVKt0odB6z6lzJ9u66AQro=; nx_ssl=2; ASID=6af24fe600000178a56138b20000004c; notSupportBrowserAlert=true; NM_THUMB_PROMOTION_BLOCK=Y; NID_SES=AAABm6DyyHK3sTk/CK/r8+BSrwLBmcb/t2L/pm+rN/XTL9cl2v+YazQyslqIhEYV5GMvm+eR3sU4zZ8ZHCo/bnLfCiMmEKkzRa7QvIYsN/DdBtCx1K4KnbQdYdJC5Fh8K1Dhwg4+o4FTalxZlLRF0DghuKq2bK3z1BSOKrw7BvbA/jfwGWT4xvJMIFumoapPMDI92pRiX965ADziS96Qe0Fl/C/AH1MxEe/oUsMcPrzfkvMSfBN2mm6jJdGMCWiwWhVVkGvoZFThUNA0MolKGmZ9CwFx2eJ/2dUMe+4CxJAnFwybfE39ytbXfV3pKgvNwNjJ77O0nmgHIkA+GvA6yF3g10BDRpyHKv+ghXOWmXv0dFNBhlZI9w3jmXC3i+Bk74W6lzInzTMfD+UgToPaXgAvSa8tEeVqndg4CtangC//E8gCdBMA0zxdGTGLn4QJ3E257tor8N40NZpJX+umNjSK3reJvRTkYe5gPrVR3W2lhaGtaKHcMoA+BAyrEFkECSX6gBSn0w9lCAuNomKhuAQ4+7conWmQAWfcHhlarylC7NN3; csrf_token=96e54b3a-f4f7-449a-9e88-8be4d491fe00',
        }
        params = (
            ('code', code),
            ('type', 'after'),
            ('isActualPointWriteExecute', 'false'),
            ('isMileageSubscriptionAlready', 'false'),
            ('isMileageSubscriptionReject', 'false'),
            ('page', index+1),
        )
        response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        movie_reviews = soup.select('body > div > div > div.score_result > ul > li')
        for index, movie_review in enumerate(movie_reviews):
            movie_score = movie_review.select_one('div.star_score > em').text
            movie_comment_tag = movie_review.select_one(f'div.score_reple > p > #_filtered_ment_{index}')
            movie_comment = movie_comment_tag.text.strip()
            if movie_comment_tag.select_one('span > a'):
                movie_comment = movie_comment_tag.select_one('span > a')['data-src'].strip()
            reviews['comments'].append(movie_comment)
            reviews['comments_score'].append(movie_score)
    movie_data[i]['reviews'] = reviews

print(movie_data)

def get_movie_reviews(counts):

    return