'''정수로 이루어진 문자열 n_str이 주어질 때,
n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.'''


# 나의 풀이
def solution(n_str):
    while True:
        if n_str[0] == '0':
            n_str = n_str[1:]
        else:
            break
    return n_str


# 다른 사람 풀이
def solution(n_str):
    return str(int(n_str))

def solution(n_str):
    return n_str.lstrip('0')