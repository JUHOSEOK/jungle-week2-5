# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

# 입력:
# 전체 테스트케이스 배열
# 반복할 갯수 n , 문자열
#
# 출력:
# 각 자리를 n번반복한 문자열


# 1. 빈배열에 테스케이스 배열의 길이 만큼 배열을 추가한다(append)
# 1.1 테스트 케이스 만큼 빈 배열을 만든다?'
# 1 반복할 개수랑 문자열길이 로 리스트 컴프리헨션써서 할수있을꺼같은데 ''join[문자하나 * 반복횟수 for 문자하나 in 문자열]  3 ABC = [AAA, BBB, CCC] = AAABBBCCC

# 2. 각각의 인덱스의 맞는 문자열의 개수만큼 반복문을 돌려 각자리의 개수만큼 문자열을 새로 추가한다.
# 2.1 그전에 반복할 갯수 * 문자열의 개수만큼의 배열의 크기를 만들어 넣는 방식으로 한다.
# 반복개수:3 , 문자열길이 3 : [0,0,0]
# 3. 리스트에 할당했던 리스트들을 출력한다.
T = int(input())

# 2
# 3 abc
#: aaabbbccc
result = []
for i in range(T):
    R, S = input().split()
    R = int(R)
    string = ''.join([ch * R for ch in S])
    result.append(string)

for i in result:
    print(i)







