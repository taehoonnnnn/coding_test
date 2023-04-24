'''문자열 binomial이 매개변수로 주어집니다.
binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다.
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.'''


# 나의 풀이
def solution(binomial):
    answer = binomial.split(' ')
    if answer[1] == '+':
        return int(answer[0]) + int(answer[2])
    if answer[1] == '-':
        return int(answer[0]) - int(answer[2])
    if answer[1] == '*':
        return int(answer[0]) * int(answer[2])
    
    
# 다른 사람 풀이
def solution(binomial):
    return eval(binomial)