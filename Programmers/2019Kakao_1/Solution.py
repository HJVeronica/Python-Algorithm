"""
실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수(not_passed) / 스테이지에 도달한 플레이어 수 (passed)

N: 전체 스테이지의 개수
stages: 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 (클리어 x,도전 중)

실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
"""


def solution(N, stages):
    players_num = len(stages)
    res_dict = {}

    for stage in range(1, N + 1):
        if players_num != 0:
            cnt = stages.count(stage)               # 해당 스테이지에서 클리어하지 못한 플레이어 수
            res_dict[stage] = cnt / players_num     # 실패율 계산
            players_num -= cnt                      # 플레이어 수 업데이트
        else:
            res_dict[stage] = 0

    # 내림차순 정렬하여 return
    return sorted(res_dict, key=lambda x: res_dict[x], reverse=True)


if __name__ == '__main__':

    n_input = int(input())
    stages_input = list(map(int, input().split(',')))

    print(solution(n_input, stages_input))
