'''정수 리스트 num_list가 주어집니다.
가장 첫 번째 원소를 1번 원소라고 할 때,
홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요.
두 값이 같을 경우 그 값을 return합니다.'''


# 나의 풀이
def solution(num_list):
    a = 0
    b = 0
    for i in range(len(num_list)):
        if i%2 == 0:
            a += num_list[i]
        else:
            b += num_list[i]
    return a if a > b else b


# 다른 사람 풀이
def solution(num_list):
    return max(sum(num_list[0: len(num_list): 2]), sum(num_list[1: len(num_list): 2]))