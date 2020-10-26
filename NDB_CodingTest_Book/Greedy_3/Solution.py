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
    # N이 K의 배수가 될 때까지 1씩 빼기
    target = (N//K) * K
    result += (N - target)
    N = target

    # N이 K보다 작아져서 더 나눌 수 없을 때 break
    if N < K:
        break

    result += 1
    N //= K

# 남은 수에 대해 1씩 빼기
result += (N - 1)
print(result)