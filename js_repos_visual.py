import requests
import plotly.express as px

# api 호출 및 응답 반환
url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"

headers = {"Accept" : "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 응답 객체 딕셔너리로 변환
response_dict = r.json()
print(f"Complete Result : {not response_dict['incomplete_results']}")

# 저장소 정보 처리
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # 저장소 명을 링크로 변환
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']

    # repo_url 이 연결된 repo_name 출력
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 툴팁 생성 - 마우스 커서를 가져갔을 시 출력되는 팝업 같은 박스
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 시각화 생성
title = "Most Starred JS Projects in Github"
labels = {'x' : 'Repository', 'y' : 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# 출력될 그래프의 텍스트 사이즈 지정
fig.update_layout(title_font_size=20, xaxis_title_font_size=20, yaxis_title_font_size=20)

# 그래프 디자인 수정
# trace : 그래프의 데이터 컬렉션 / marker_color : 마커의 색상 (CSS에서 이름이 붙은 색상 사용 가능) / opacity :불투명도 (0 to 1)
fig.update_traces(marker_color='Maroon', marker_opacity=0.6)

fig.show()