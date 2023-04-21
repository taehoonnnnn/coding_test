'''정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.'''


# 나의 풀이
def solution(num_list):
    a = 0
    b = 1
    for i in num_list:
        a += i
        b *= i
        
    return 1 if a*a > b else 0