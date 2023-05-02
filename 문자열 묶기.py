'''문자열 배열 strArr이 주어집니다.
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 ,
장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.'''


# 나의 풀이
def solution(strArr):
    answer = []
    for i in sorted(strArr, key=len):
        if not answer or len(i) != len(answer[-1][0]):
            answer.append([i])
        else:
            answer[-1].append(i)
    return max([len(i) for i in answer])


# 다른 사람 풀이
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)


def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())