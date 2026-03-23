# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

# 아이디어 : bfs로 탐색해 처음에 1에 관련된 것들을 감염시켜놓고 그와 연결되어있다면 카운트증가 단 또 방문한거 queue에 넣으면안됨

#입력
# 1. 컴퓨터수
# 2. 컴퓨터간의 쌍의수
# 3. 연결된 컴퓨터 리스트들
#
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
from collections import deque
computer_num = int(input())
pair_num = int(input())
graph = {i: [] for i in range(1, computer_num + 1)}


for _ in range(pair_num):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


visitied = []

queue = deque([1])
visitied.append(1)

while queue:
    key = queue.popleft()

    for neighbor in graph[key]:
        if neighbor not in visitied:
            visitied.append(neighbor)
            queue.append(neighbor)


print(len(visitied)-1)
print(graph)
print(sorted(visitied))


