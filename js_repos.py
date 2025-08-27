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

# 받아온 저장소 분석
print("Selected information about each Repository:")
for repo_dict in repo_dicts:
    print(f"\n Selected information about first repository: ")
    print(f"Name : {repo_dict['name']}")
    print(f"Owner : {repo_dict['owner']['login']}")
    print(f"Stars : {repo_dict['stargazers_count']}")
    print(f"Repository : {repo_dict['html_url']}")
    print(f"Created : {repo_dict['created_at']}")
    print(f"Updated : {repo_dict['updated_at']}")
    print(f"Description : {repo_dict['description']}")

# 결과 처리
print(response_dict.keys())