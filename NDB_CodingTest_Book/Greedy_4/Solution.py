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

N = int(input())
X = list(map(int, input().split()))
result = 0

# 공포도 오름차순 정렬
heapq.heapify(X)

while X:
    # 가장 작은 공포도 꺼내기
    x = heapq.heappop(X)
    group = list()

    if x == 1:  # 공포도가 1일 경우엔 혼자 그룹지어주기
        group.append(x)
    else:
        group.append(x)
        for _ in range(x - 1):  # 공포도 숫자만큼 개수 맞춰서 넣어주기
            group.append(heapq.heappop(X))
            if not X:  # 넣는 도중 더이상 pop할 것이 없으면 break
                break

    # group에서 가장 큰 값이 group의 길이보다 작을 경우
    if max(group) <= len(group):
        result += 1

    group.clear()  # group 리스트 초기화

print(result)
