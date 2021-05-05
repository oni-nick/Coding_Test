'''
목표: 경우의수 만큼 계산 후 최댓값 찾기
'''
import itertools
def solution(expression):
    answer = 0
    max_ = 0
    op_count = set([])  # 연산자 종류 확인을 위한 set 자료형
    for i in expression:
        if (i == '+') or (i == '-') or (i == '*'):
            op_count.add(i)
    cases = list(itertools.permutations(op_count, len(op_count)))
    for c in cases:
        postfix = infix_to_postfix(expression, c)
        result = calculate_postfix(postfix)
        max_ = max(result, max_)
    answer = max_
    print(answer)
    return answer


def priority_op(op):
    if op == '-':
        return 0
    elif op == '+':
        return 1
    elif op == '*':
        return 2


def calculate_postfix(postfix):
    stack = []
    for i in postfix:
        if (i != '+') and (i != '-') and (i != '*'):  # 숫자일 때,
            stack.append(i)
        else:  # 연산자일 때,
            second = int(stack.pop())  # 아 연산의 우선순위가 틀렸구나 !! s- f (틀림)
            first = int(stack.pop())
            if i == '+':
                stack.append(first + second)
            elif i == '-':
                stack.append(first - second)
            elif i == '*':
                stack.append(first * second)
    return abs(stack.pop())


def infix_to_postfix(exp, case):
    exp = "".join(exp)
    num = ""
    op_stack = []
    postfix = []
    ######################################
    for i in exp:
        if (i != '+') and (i != '-') and (i != '*'):  # 숫자일 때,
            num = num + i
        else:  # 연산자일 때,
            postfix.append(num)
            while op_stack and case.index(op_stack[-1]) >= case.index(i):  # op_stack이 비어있지 않고, 현 연산자보다 우선순위가 높을 때
                postfix.append(op_stack.pop())
            op_stack.append(i)
            num = ""
    postfix.append(num)  # 마지막 피연산자 추가
    while op_stack:   # op_staack 빌 때까지 실행한다.
        postfix.append(op_stack.pop())  # 이얏!! 역시  op_stack에 남아있을줄 알았엉
    ####################################
    return postfix

solution("100-200*300-500+20")