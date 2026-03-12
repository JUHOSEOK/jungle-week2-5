import math
# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

# 입력:
# 문자열개수 Q
# 문자열:
# 8
# 10
# 16
#
# 1. 숫자 받아 배열에 넣는다.
# 2. 2로 나눠서 +1을 해가며 둘다 소수인 경우를 찾는다.


def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # for i in range(2,math.sqrt(n)):
    #     if n % i == 0:
    #         return False

    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False

    return True


def gold_bar(S):
    D = S // 2
    left = D
    right = D
    while True:
        if is_prime(left) and is_prime(right):
            return left, right
        else:
            left = left -1
            right += 1


Q = int(input())
S = []
for i in range(Q):
    s = int(input())
    S.append(s)

for i in range(len(S)):
    a ,b = gold_bar(S[i])
    print(a , b)







