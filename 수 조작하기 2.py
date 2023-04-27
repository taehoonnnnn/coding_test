'''정수 배열 numLog가 주어집니다.
처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을,
입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

"w" : 수에 1을 더한다.
"s" : 수에 1을 뺀다.
"d" : 수에 10을 더한다.
"a" : 수에 10을 뺀다.
그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다.
즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.'''


# 나의 풀이
def solution(numLog):
    cnt = numLog[0]
    result = ''
    for i in numLog:
        if cnt+1 == i:
            cnt += 1
            result += 'w'
            
        elif cnt+10 == i:
            cnt += 10
            result += 'd'
            
        elif cnt-1 == i:
            cnt -= 1
            result += 's'
            
        elif cnt-10 == i:
            cnt -= 10
            result += 'a'
        
    return result


# 다른 사람 풀이
def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1] # 현재 값과 이전 값의 차이를 계산
        if diff == 1:
            answer += 'w' # 1 더하기
        elif diff == -1:
            answer += 's' # 1 빼기
        elif diff == 10:
            answer += 'd' # 10 더하기
        elif diff == -10:
            answer += 'a' # 10 빼기
    return answer