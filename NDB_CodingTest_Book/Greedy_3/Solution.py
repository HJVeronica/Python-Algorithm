"""
### 동빈나 <이것이 코딩테스트다> 실전 문제
## 그리디 알고리즘 - 3. 1이 될 때까지

# 난이도 '하' / 시간제한 1초 / 메모리 제한 128MB / 기출: 2018 E 기업 알고리즘 대회
# 풀이 시간제한: 30분
"""

"""
N: 1로 만들 숫자 
K: N을 나눌 숫자 

Result: 주어진 N이 1이 될 때까지 걸리는 최소 횟수
"""

N, K = map(int, input().split())
result = 0

while True:
    if N == 1:
        break

    if N % K == 0:
        N /= K
    else:
        N -= 1
    result += 1

print(result)