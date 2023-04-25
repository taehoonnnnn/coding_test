'''정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다.
예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

10 / 2 = 5
(5 - 1) / 2 = 4
4 / 2 = 2
2 / 2 = 1
위와 같이 4번의 나누기 연산으로 1이 되었습니다.
정수들이 담긴 리스트 num_list가 주어질 때,
num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.'''


# 나의 풀이
def solution(num_list):
    cnt = 0
    for i in range(len(num_list)):
        while True:
            if num_list[i] != 1:
                if num_list[i]%2 == 0:
                    num_list[i] = num_list[i] // 2
                    cnt += 1
                else:
                    num_list[i] = (num_list[i] - 1) // 2
                    cnt += 1
            else:
                break
    return cnt


# 다른 사람 풀이
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)