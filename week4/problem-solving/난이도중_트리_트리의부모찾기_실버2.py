# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
# 1번 노드에서 시작해 연결된 노드를 탐색 하면서, 새로 방문한 노드의 부모를 현재 노드로 기록한다.
# ex)
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
import sys

from collections import deque
input = sys.stdin.readline
n = int(input())

pair_num = n-1
graph = {i : [] for i in range(1, n+1) }

for _ in range(pair_num):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

# print(graph)
queue = deque([1])
visited = [False] * (n + 1)
# visited = []
# visited = [False] * (n + 1): "너 방문했니?"라고 물어볼 때, 리스트 전체를 뒤지는 게 아니라 해당 번호의 칸만 딱 확인하기 때문에 속도가 빛의 속도(O(1))로 빨라집니다.

result = [0] * (n + 1)
while queue:
    key = queue.popleft()

    for neighbor in graph[key]:
        if  not visited[neighbor]:
        # in neighbor not in visited:
            result[neighbor] = key
            queue.append(neighbor)
            visited[neighbor] = True
            # visited.append(neighbor)

lenth = len(result)
for i in range(2, lenth):
    print(result[i])



