"""
n: 전체 학생 수
lost: 체육복을 도난당한 학생들의 번호가 담긴 배열
reserve: 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열

return: 체육수업을 들을 수 있는 학생의 최댓값
"""


def solution(n, lost, reserve):
    reserve_ = [x for x in reserve if x not in lost]
    lost_ = [x for x in lost if x not in reserve]

    for i in reserve_:
        if (i - 1) in lost_:
            lost_.remove(i - 1)
        elif (i + 1) in lost_:
            lost_.remove(i + 1)

    return n - len(lost_)


if __name__ == '__main__':

    N = int(input())
    lostArr = list(map(int, input().split()))
    reverseArr = list(map(int, input().split()))

    print(solution(N, lostArr, reverseArr))
