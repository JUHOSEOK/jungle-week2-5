# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
from collections import deque
# 입력:
# 1. 보드의 크기 N ex) N x N
# 2. 사과의 개수 K개
# 3. 사과의 위치 K ex)3 4
# 4. 뱀의 방향 변환 횟수 L
# 5. L개의 줄에 뱀의 방향 변환 정보
#
# 출력:
# 벽에 밖았을때(게임오버) 시간
#
# 1. 입력받은 N만큼 이중배열 만들고 0으로 초기화한다.
# 2. 사과개수 입력받는다
# 3. 사과 위치의 이중배열에 1로 넣는다.
# 4. 방향 변환횟수 받는다.
# 5. 방향 횟수 만큼 0,0 부터 y 좌표 1씩 이동시키고 d면은 오른쪽이동 L이면 왼쪽이동하고 이동 횟수 추가한다.
# 6. x혹은 y가 6이 되거나 몸끼리 부딪히면 종료하 이동횟수 출력한다.


def get_dir(rotate, dir):

    if rotate == 'D':
        dir = (dir + 1) % 4
    elif rotate == 'L':
        dir = (dir - 1 + 4) % 4
    return dir

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())
arr = [[0] * N for _ in range(N)]

K = int(input())
for i in range(K):
    apple = input().split()
    ax = int(apple[0])
    ay = int(apple[1])
    arr[ax-1][ay-1] = 1

L = int(input())
x = 0
y = 0

dir = 0
snake_tail = []
snake_tail = deque(snake_tail)
cnt = 0
commands = {}

# 미리 시간초를 다 받아놓음
# 원래 나는 만약에 3 D, 15 L 이 커멘드로 주어졌다면 3초 가고 15초 가고 총 18초 이런식으로 알았는데
# 3초 가고 15초 시간되었을때 그니까 총 15초 동안 일어나는 일이라 그럼

for i in range(L):
    rotate = input().split()
    # ex) 5 D, 3 L
    commands[int(rotate[0])] = rotate[1]


# 처음에 머리를 생성시켜줌
# 왜냐하면 00 에서 01 로 갈때 사과가없으면 꼬리를 잘라야 하는데 00으로 하지않으면 자를 꼬리가 없어짐
snake_tail.append((0,0))
while True:
    # for k in range(int(rotate[0])):
        # if 벽부딪히거나 추가했던거에 도달하면:

    x = int(x) + int(dx[dir])
    y = int(y) + int(dy[dir])

    cnt += 1

    # snake_tail in 쓰면 어떤식으로 출력되는거지
    if (x >= N or x < 0 or y >= N or y < 0) or (x, y) in snake_tail:
        break

    snake_tail.append((x,y))

    if arr[x][y] == 1:
        arr[x][y] = 0
    else:
        snake_tail.popleft()

    if cnt in commands.keys():
        dir = get_dir(commands[cnt], dir)

    # dir = get_dir(rotate[1], dir)
    # print("dir",dir)
    # print(snake_tail)
    # print(x,y)

print(cnt)


















