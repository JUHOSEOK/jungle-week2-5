# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

# 입력:
# 1.입력에 들어올 문자개수 ex) 4
# 2.문자열들  ex) las \n god \n psala \n sal
#
# 출력:
# 1.문자열의 길이, 2.가운데 문자
#
# 1. 받을 문자열의 개수를 입력받는다
# 2. 문자열의 개수만큼 문자열을 리스트에 넣는다.
# 3. 리스트에 있는 문자열을 차례대로 set함수에 넣는다.
# 4. set함수에 리스트의 문자열들을 뒤집어 그 문자열이 있는지 확인한다. 아니면 그 문자열을 뒤집었을때 똑같은지 확인하고 맞으면 출력한다.

S = int(input())

arr = [input() for _ in range(S)]

set_arr = set(arr)


for i in range(S):
    reverse_s = arr[i]
    reverse_s = reverse_s[::-1]
    # print("셋함수", reverse_s)
    if reverse_s in set_arr:
        result = reverse_s

middle_s = len(result) // 2

print(len(result), result[middle_s])

