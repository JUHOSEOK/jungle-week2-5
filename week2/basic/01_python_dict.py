"""
[파이썬 기본 문법 - 리스트와 딕셔너리 활용]

문제 설명:
- 학생들의 이름과 점수를 입력받아 평균 점수 이상인 학생들을 찾아 출력합니다.
- 파이썬의 기본 자료구조인 리스트와 딕셔너리를 활용하는 문제입니다.

입력:
- students: 학생 정보를 담은 딕셔너리 리스트
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

출력:
- 평균 점수
- 평균 이상인 학생들의 이름 리스트

예제:
입력:
[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

출력:
평균 점수: 87.5
평균 이상 학생: ['Bob', 'David']

힌트:
- sum() 함수와 len() 함수를 활용하세요
- 리스트 컴프리헨션을 사용하면 간결하게 작성할 수 있습니다
"""

def find_above_average_students(students):
    """
    평균 점수 이상인 학생들을 찾는 함수
    
    Args:
        students: 학생 정보 딕셔너리 리스트
    
    Returns:
        tuple: (평균 점수, 평균 이상 학생 이름 리스트)
    """


    # TODO: 모든 학생의 점수를 리스트로 추출하세요
    pass
    # 배열안에 있는 딕셔너리가있을텐데 그 딕셔너리 값을 어떻게 접근하지?
    # students1[0][score]
    # 리스트 컴프리헨션이 뭐지?
    # 리스트안에서 표현식이나, 조건문을 통해 원래는 1.배열 초기화 2.값 저장 에 순서를 거쳐야하지만 리스트 안에서 이걸 한번에 해결하는 list comprehension 굳이 직역하면 리스트 이해력? 인데 의미가 안맞아


    # TODO: 평균 점수를 계산하세요
    # 리스트를 인자로 받아오면 거기서 socre만 다시 리스트로 만듬
    # 리스트만 받아온 배열에서 sum()함수써서 총 점수 구함
    # 리스트만 받아온 배열의 길이가 학생의 수니까 총길이 도구함
    # 둘이 나눠서 구함 평균점수

    pass
    scoreList = [i["score"] for i in students ]
    above_average_students = []
    sumScore = sum(scoreList)
    length = len(scoreList)
    average = sumScore / length

    # TODO: 평균 이상인 학생들의 이름을 리스트로 추출하세요
    # 학생점수 배열을 평균이상 넘는다면
    # 학생리스트 받아온 배열에서 값을 추가해줌
    stuList = [i["name"] for i in students]

    for i in range(length):
        if scoreList[i] >= average:
            above_average_students.append(stuList[i])

    return average, above_average_students

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]
    
    avg, students = find_above_average_students(students1)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
    print()
    
    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90}
    ]
    
    avg, students = find_above_average_students(students2)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")


