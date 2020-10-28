"""
### 동빈나 <이것이 코딩테스트다> 기출 문제
## 그리디 알고리즘 - 2. 곱하기 혹은 더하기

# 난이도 '하' / 시간제한 1초 / 메모리 제한 128MB / 기출: Facebook 인터뷰
# 풀이 시간제한: 30분
"""

"""
S: 여러 개의 숫자로 구성된 하나의 문자열 (0-9)

Result: * 또는 + 연산자를 숫자 사이에 넣어 가장 큰 수를 구하는 프로그램 (무조건 왼->오 순서로만 연산)
"""
import time
from collections import deque

start_time = time.time()    # 시간 측정 시작

S = deque(list(map(int, input())))
result = S.popleft()    # 가장 첫 수는 미리 넣어두기

while S:
    num = S.popleft()

    # 연산을 진행할 숫자 두 개가 0 또는 1 값을 가질 경우, + 연산으로 더 큰 수를 만들 수 있음
    if (result <= 1) or (num <= 1):
        result += num
    else:   # 그 외 숫자는 모두 곱셈
        result *= num

print(result)

end_time = time.time()  # 시간 측정 종료
print("프로그램 수행 시간: ", end_time - start_time)    # 수행 시간 출력
