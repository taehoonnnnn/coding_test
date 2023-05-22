'''두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.'''


# 나의 풀이
def solution(n, m):
    answer = []
    for i in range(min(n,m), 0, -1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
    for i in range(max(n,m), (n*m)+1):
        if i%n==0 and i%m==0:
            answer.append(i)
            break
    return answer


# 다른 사람 풀이
import math

def solution(n, m):
    su1 = math.gcd(n,m)
    su2 = n * m // su1
    return su1, su2