"""
### 동빈나 <이것이 코딩테스트다> 기출 문제
## 그리디 알고리즘 - 5. 볼링공 고르기

# 난이도 '하' / 시간제한 1초 / 메모리 제한 128MB / 기출: 2019 SW 마에스트로 입학 테스트
# 풀이 시간제한: 30분
"""

'''
N: 볼링공의 개수 (1~)
M: 볼링공의 최대 무게 (1 ~ 10)
K: 각 볼링공의 무게 (같은 무게의 공도 서로 다른 공으로 간주)

Result: A, B가 서로 무게가 다른 볼링공을 고르는 경우의 수 
'''
import time

start_time = time.time()    # 시간 측정 시작

N, M = map(int, input().split())
K = list(map(int, input().split()))
result = 0
# combinationArr = list()   # 조합 확인용 리스트

for i in range(len(K)-1):
    for j in range(i+1, len(K)):
        if K[i] == K[j]:
            continue
        result += 1
        #combinationArr.append((K[i], K[j]))

print(result)
#print(combinationArr)

end_time = time.time()  # 시간 측정 종료
print("프로그램 수행 시간: ", end_time - start_time)    # 수행 시간 출력
