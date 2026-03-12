# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 입력 : 문자열
# ex) Mississipi
#출력 : 입력된 문자열중 가장많이 사용된 알파벳
# 조건 : 가장많이 사용된 알파벳이 여러개 존재하면 ? 출력
# ex) ?

# 1. 문자열을 입력받는다
# 2. 문자열을 문자 아스키코드로 변환해 그자리에 배열에 1 추가한다. A : 65 Z : 90
# 3. 배열 다 돌려서 두개의 변수로 비교해가면서 마지막까지 반복하는데
# 3.1 max값이 현재값하고 같은지 검사하고 같다면 True바꾸고
# 3.2 마지막에 maxNum이 크다면 False로 바꾸고 그 자리에 인덱스를 문자로 변환해서 출력하고 아니라면 ? 출력하고

# 3417
# 3131 중복검사를 맨처음에 하고 True로 바꿔나야하나 중복이 있을때는 판별을 못하잖아 maxNum -1 로 하고 배열현재값 비교하는데 현재값이 크면 maxNum에 넣고 +1 해야하나
# 3120

# 40 41 42 42 41 42 42 41 44 41
#
# 1 4 4 1

mostUsed = [0] * 127
S = input()

for i in range(len(S)):
    upperS = S[i].upper()
    char = ord(upperS)
    # print(upperS)
    mostUsed[char] += 1

maxNum =0
maxIndex = 0
isduplication = False

for i in range(65, 91):
    if maxNum == mostUsed[i] and maxNum != 0:
        isduplication = True

    if maxNum < mostUsed[i]:
        maxNum = mostUsed[i]
        maxIndex = i
        isduplication = False


if isduplication:
    print("?")
else:
    print(chr(maxIndex))

