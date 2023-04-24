'''문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다.
myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중,
pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.'''


# 나의 풀이
def solution(myString, pat):
    myString = myString.replace("A","C")
    myString = myString.replace("B","A")
    myString = myString.replace("C","B")

    return int(pat in myString)


# 다른 사람 풀이
def solution(myString, pat):
    pat=list(pat)
    for i in range(len(pat)):
        if pat[i]=='B':
            pat[i]='A'
        else: pat[i]='B'
    if ''.join(pat) in myString: return 1
    return 0