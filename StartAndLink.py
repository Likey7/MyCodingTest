# 2024. 02. 20
# 백준 14889번 스타트와 링크 
# https://www.acmicpc.net/problem/14889

# 풀이시간 : 51분(조합 방법)
# 시간제한 / 메모리제한 : 2초 / 128MB
# 실행시간 / 메모리사용 : 0.17초 / 5.6MB

#풀이 1 조합 방법
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)

#팀의 능력치 계산
def chemi(team, S):
    ability = 0
    for i in team:
        for j in team:
            ability += S[i][j]
    return ability

players = range(N)
for start_team in combinations(players, N // 2):
    # 스타트 팀을 제외한 나머지 팀
    link_team = tuple(set(players) - set(start_team))

    # 두 팀의 능력치 계산
    start_ability = chemi(start_team, S)
    link_ability = chemi(link_team, S)
    
    # 능력치 차이의 절대값
    diff = abs(start_ability - link_ability)
    answer = min(answer, diff)

print(answer)


####################################################################################
# 풀이2 백트래킹 방법

def backtrack(idx, first_team, second_team):
    global answer
    # 기저 조건: 팀이 완성된 경우, 능력치 계산
    if idx == N:
        if len(first_team) == N // 2 and len(second_team) == N // 2:
            # 두 팀의 능력치 계산
            first_ability = sum([S[i][j] for i in first_team for j in first_team])
            second_ability = sum([S[i][j] for i in second_team for j in second_team])
            # 능력치 차이의 절대값 계산 후 최소 차이 업데이트
            diff = abs(first_ability - second_ability)
            answer = min(answer, diff)
        return

    # 현재 인덱스의 선수를 첫 번째 팀에 배정
    if len(first_team) < N // 2:
        first_team.append(idx)
        backtrack(idx + 1, first_team, second_team)
        first_team.pop()  # 백트래킹

    # 현재 인덱스의 선수를 두 번째 팀에 배정
    if len(second_team) < N // 2:
        second_team.append(idx)
        backtrack(idx + 1, first_team, second_team)
        second_team.pop()  # 백트래킹

# 새로운 입력값
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 전역 변수로 최소 능력치 차이 초기화
answer = int(1e9)

# 백트래킹 실행
backtrack(0, [], [])

print(answer)
