# 2024. 02. 15
# 백준 1697번 숨바꼭질 
# https://www.acmicpc.net/problem/1697

# 풀이시간 : 54분
# 시간제한 / 메모리제한 : 2초 / 128MB
# 실행시간 / 메모리사용 :  0.1초 / 34.4MB

from collections import deque

def bfs(N, M):
    #최대 위치 설정
    max_position = 100001
    #방문 및 시간 기록 배열
    visited = [0] * max_position

    q = deque([N])

    while q:
        position = q.popleft()

        if position==M:
            return visited[position]

        # 이동가능한 세가지 경우의 수 탐색
        for next_position in (position-1, position+1, position*2):
            #위치가 제한범위 내이고, 미방문위치인지 확인
            if 0 <= next_position < max_position and not visited[next_position]:
                visited[next_position] = visited[position] + 1
                q.append(next_position)

# 입력
N, M = map(int, input().split())
# 출력
print(bfs(N, M))