import requests

# api 호출 및 응답 반환
url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"
headers = {"Accept" : "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 응답 객체 딕셔너리로 변환
response_dict = r.json()
print(f"Total repositories : {response_dict['total_count']}")
print(f"Complete results : {not response_dict['incomplete_results']}")

# 저장소 정보 탐색
repo_dicts = response_dict['items']
print(f"Repositories returned : {len(repo_dicts)}")

# 첫 번째 저장소 분석
repo_dict = repo_dicts[0]
print(f"\nKeys : {len(repo_dict)}")
for key in repo_dicts[0]:
    print(key)

# 결과 처리
print(response_dict.keys())