'''이차원 정수 배열 arr이 매개변수로 주어집니다. arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고,
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.'''


# 내 풀이
def solution(arr):
    while True:
        if len(arr) > len(arr[0]):
            for i in range(len(arr)):
                arr[i].append(0)
        elif len(arr) < len(arr[0]):
            for i in range(len(arr[0])-len(arr)):
                arr.append(len(arr[0])*[0])
        else:
            break
    return arr


# 다른 사람 풀이
def solution(arr):
    answer = []

    countMax = max(len(arr), max(len(row) for row in arr))
    i = 0
    while i < countMax:
        if i < len(arr):
            answer.append(arr[i] + [0] * (countMax - len(arr[i])))
        else:
            answer.append([0] * countMax)
        i += 1

    return answer