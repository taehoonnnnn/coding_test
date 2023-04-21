'''한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.'''


# 나의 풀이
def solution(num_str):
    return sum([int(i) for i in num_str])

# 다른 사람 풀이
def solution(num_str):
    return sum(map(int, list(num_str)))