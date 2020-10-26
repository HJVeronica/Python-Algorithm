"""
### 동빈나 <이것이 코딩테스트다> 실전 문제
## 그리디 알고리즘 - 2. 숫자 카드 게임

# 난이도 '하' / 시간제한 1초 / 메모리 제한 128MB / 기출: 2019 국가 교육기관 코딩 테스트
# 풀이 시간제한: 30분
"""

"""
N * M: 숫자가 쓰인 카드가 놓인 이차원 배열 크기

Result: 가장 높은 숫자가 쓰인 카드 한 장을 뽑기
"""

N, M = map(int, input().split())
result = 0

for i in range(N):
    cardsInRow = list(map(int, input().split()))
    minCard = min(cardsInRow)

    result = max(result, minCard)

print(result)
