'''정수 배열 arr가 주어집니다.
arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고,
50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.'''


# 나의 풀이
def solution(arr):
    answer = []
    for i in arr:
        if i%2 == 0 and i >= 50:
            answer.append(i//2)
        elif i%2 != 0 and i < 50:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer


# 다른 사람 풀이
def solution(arr):
    return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]