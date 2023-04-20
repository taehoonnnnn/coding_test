'''정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.'''


# 내 풀이
def solution(n):
    answer = [[]]
    del answer[0]
    for i in range(n):
        answer.append(n*[0])
        
    for i in range(n):
        answer[i][i] = 1
        
    return answer