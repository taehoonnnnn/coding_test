'''영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
문자열 numbers가 매개변수로 주어질 때,
numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.'''


# 나의 풀이
def solution(numbers):
    answer = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    a = ''
    b = []
    for i in numbers:
        a += i
        if a in answer:
            b.append(answer[a])
            a = ''
    return int(''.join(b))


# 다른 사람 풀이
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])

    return int(numbers)