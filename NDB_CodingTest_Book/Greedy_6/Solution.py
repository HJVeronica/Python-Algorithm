"""
### 동빈나 <이것이 코딩테스트다> 기출 문제
## 그리디 알고리즘 - 3. 문자열 뒤집기

# 난이도 '하' / 시간제한 2초 / 메모리 제한 128MB / 기출: 핵심 유형 (https://www.acmicpc.net/problem/1439)
# 풀이 시간제한: 20분
"""

"""
S: 0과 1로만 이루어진 문자열

Result: 연속된 하나 이상의 숫자를 뒤집어서 모두 같은 숫자로 만들기 위해 필요한 행동의 최소 횟수
"""
import time

start_time = time.time()    # 시간 측정 시작

cnt = [0, 0]    # index 0: 0 to 1, index 1: 1 to 0

S = list(map(int, input()))
prevNum = S[0]

if prevNum == 0:
    cnt[0] += 1
else:
    cnt[1] += 1

for i in range(1, len(S)):
    if prevNum != S[i]:     # 숫자가 바뀌면 카운트
        cnt[S[i]] += 1
    prevNum = S[i]

print(min(cnt))

end_time = time.time()  # 시간 측정 종료
print("프로그램 수행 시간: ", end_time - start_time)    # 수행 시간 출력
