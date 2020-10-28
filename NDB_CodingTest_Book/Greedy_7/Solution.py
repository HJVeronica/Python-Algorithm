"""
### 동빈나 <이것이 코딩테스트다> 기출 문제
## 그리디 알고리즘 - 4. 만들 수 없는 금액

# 난이도 '하' / 시간제한 1초 / 메모리 제한 128MB / 기출: K 대회 기출
# 풀이 시간제한: 30분
"""

"""
N: 동전의 개수 
coinUnits: 각 동전의 화폐 단위를 나타내는 N개의 자연수를 담은 배열 

Result: 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값 
"""
import time
import heapq

start_time = time.time()    # 시간 측정 시작

N = int(input())
coinUnits = list(map(int, input().split()))
heapq.heapify(coinUnits)    # 오름차순 정렬

result = 1

while coinUnits:
    num = heapq.heappop(coinUnits)
    if result < num:    # 덧셈 조합에서 중간에 비는 숫자가 생기는 경우
        break
    result += num

print(result)

end_time = time.time()  # 시간 측정 종료
print("프로그램 수행 시간: ", end_time - start_time)    # 수행 시간 출력
