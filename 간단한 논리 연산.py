'''boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때,
다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

(x1 ∨ x2) ∧ (x3 ∨ x4)'''


# 나의 풀이
def solution(x1, x2, x3, x4):
    answer1 = False
    answer2 = False
    if x1 == True or x2 == True:
        answer1 = True
    if x3 == True or x4 == True:
        answer2 = True
    return True if answer1 == True and answer2 == True else False


# 다른 사람 풀이
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)