"""
### 동빈나 <이것이 코딩테스트다> 기출 문제
## 그리디 알고리즘 - 1. 모험가 길드

# 난이도 '하' / 시간제한 1초 / 메모리 제한 128MB / 기출: 핵심 유형
# 풀이 시간제한: 30분
"""

"""
N: 모험가 수
X: 각 모험가의 공포도를 담은 배열 (X의 각 원소 <= N)

Result: 모험가 그룹을 만들 수 있는 최대 개수
"""

import heapq
import time

start_time = time.time()    # 시간 측정 시작

N = int(input())
X = list(map(int, input().split()))
result = 0
count = 0

# 공포도 오름차순 정렬
heapq.heapify(X)

for i in X:
    count += 1

    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도와 크거나 같을 경우 그룹화
    if count >= i:
        result += 1
        count = 0

print(result)

end_time = time.time()  # 시간 측정 종료
print("프로그램 수행 시간: ", end_time - start_time)    # 수행 시간 출력