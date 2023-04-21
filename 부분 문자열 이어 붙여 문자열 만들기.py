'''길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.'''


# 내 풀이
def solution(my_strings, parts):
    return ''.join([i[j[0]:j[1]+1] for i, j in zip(my_strings, parts)])


# 다른 사람 풀이
def solution(my_strings, parts):
    return ''.join(my_strings[i][parts[i][0]:parts[i][1]+1] for i in range(len(my_strings)))