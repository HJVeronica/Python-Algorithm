"""
### 동빈나 <이것이 코딩테스트다> 실전 문제
## 그리디 알고리즘 - 1. 큰 수의 법칙

# 난이도 '하' / 시간제한 1초 / 메모리 제한 128MB / 기출: 2019 국가 교육기관 코딩 테스트
# 풀이 시간제한: 30분
"""

"""
N: 배열의 크기
M: 숫자가 더해지는 횟수
K: 연속으로 더해지는 횟수 제한

Result: 주어진 수들을 M번 더해 가장 큰 수를 구하기
"""

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

nums.sort(reverse=True)

maxNum = nums[0]
secondNum = nums[1]

while True:
    if M == 0:
        break

    for _ in range(K):
        if M == 0:
            break
        result += maxNum
        M -= 1

    result += secondNum
    M -= 1

print(result)
"""
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

nums.sort(reverse=True)

maxNum = nums[0]
secondNum = nums[1]

# 가장 큰 수를 더하는 횟수
cnt = (M // (K+1)) * K
# 나누어 떨어지지 않을 때 더할 횟수도 추가
cnt += M % (K+1)

result += (cnt * maxNum)
result += ((M-cnt) * secondNum)

print(result)
"""