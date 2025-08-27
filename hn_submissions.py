from operator import itemgetter

import requests

# api 호출 및 응답 확인
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 각 글의 정보 처리
submission_ids = r.json()
submission_dicts = []

# 상위 30개의 글 확인
for submission_id in submission_ids[:30]:
    # 글을 순회하며 api 호출
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id : {submission_id}'s Status Code: {r.status_code}")
    response_dict = r.json()
    try:
        # 각 글에 대한 딕셔너리 생성
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        continue


submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"Title : {submission_dict['title']}")
    print(f"Discussion Link : {submission_dict['hn_link']}")
    print(f"Comments : {submission_dict['comments']}")