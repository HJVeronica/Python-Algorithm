"""
d: 부서별로 신청한 금액이 들어있는 배열
budget: 예산

return: 최대 몇 개의 부서에 물품을 지원할 수 있는지
"""


def solution(d, budget):
    # 모든 부서에 물품을 지원할 수 있는 경우 d의 길이 바로 return
    if budget >= sum(d):
        return len(d)

    d.sort()        # d 오름차순 정렬
    answer = 0
    sum_d = 0

    for i in d:
        # 예산 초과할 경우 함수 종료
        if (sum_d + i) > budget:
            return answer
        sum_d += i      # 누적 금액 계산
        answer += 1     # 지원 가능한 부서 개수 카운트


if __name__ == '__main__':

    d_input = list(map(int, input().split()))
    budget_input = int(input())

    print(solution(d_input, budget_input))
