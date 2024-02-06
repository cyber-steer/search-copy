import json

# 파일 열기
with open('extension.json', 'r') as f:
    data = json.load(f)

# data는 이제 파이썬 딕셔너리입니다.
for key, val in data.items():
    print(key, end=", ")
