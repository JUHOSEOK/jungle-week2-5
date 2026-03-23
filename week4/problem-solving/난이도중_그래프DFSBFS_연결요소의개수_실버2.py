# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

# 그래프들을 bfs하여 탐색 할때 연결되어있는 집합의 수 구하기
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


queue = deque()
visited = [False] * (n+1)
group = 0

for i in range(1, n+1):
    # print(f"정점 {i} 확인 중, 방문 여부: {visited[i]}")
    if visited[i]: continue
    queue.append(i)
    visited[i] = True
    while queue:

        key = queue.popleft()
        # print(f"현재 방문 중인 노드: {key}")


        for neighbor in graph[key]:
            if not visited[neighbor]:

                queue.append(neighbor)
                visited[neighbor] = True



    group += 1


print(group)
# print(visited)