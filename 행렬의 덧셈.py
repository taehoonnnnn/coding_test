'''행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.'''


# 나의 풀이
def solution(arr1, arr2):
    answer = []
    a = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            a.append(arr1[i][j]+arr2[i][j])
        answer.append(a)
        a = []
    return answer


# 다른 사람 풀이
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer