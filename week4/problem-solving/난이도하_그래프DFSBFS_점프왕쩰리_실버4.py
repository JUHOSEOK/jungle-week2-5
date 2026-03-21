# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 아이디어: bfs로 탐색하고 그값이 -1이 라면 출력하고 아니라면 뺀값의 좌표를 통해 jump값을 휙득하고 처음에 0,0을 예로들면 0,1 과 1,0 을 queue에 append하기전에
# 만약 점프 적용한 두 좌표값이 격자를 벗어나지 않고 visited배열안에 없다면 visited에 점프한 두 좌표값을 true로 만들고 queue에 추가

import sys
from collections import deque
n = int(sys.stdin.readline())

def is_range(arr1, arr2, n):
    return arr1 >= 0 and arr1 < n and arr2 >= 0 and arr2 < n


grid = []
for _ in range(n):
    # 한 줄을 읽어서 공백으로 나누고 숫자로 변환하여 리스트로 만듦
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

queue = deque([(0,0)])

visited = [[False] * n for _ in range(n)]
visited[0][0] = True
while queue:

    x, y = queue.popleft()
    if grid[x][y] == -1:
        print("HaruHaru")
        sys.exit()

    jump = grid[x][y]

    right_x = x
    right_y = y + jump

    down_x = x + jump
    down_y = y

    if is_range(right_x, right_y, n) and  not visited[right_x][right_y]:

            visited[right_x][right_y] = True
            queue.append((right_x,right_y))

    if is_range(down_x, down_y, n) and not visited[down_x][down_y]:
            visited[down_x][down_y] = True
            queue.append((down_x, down_y))

print("Hing")



