import requests
import json

# api 요청을 보내고 응답 저장
url = "https://hacker-news.firebaseio.com/v0/item/1227.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 데이터 구조
response_dict= r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)