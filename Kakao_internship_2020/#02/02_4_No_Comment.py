import itertools
def solution(expression):
    answer = 0
    max_ = 0
    op_count = set([])
    for i in expression:
        if (i == '+') or (i == '-') or (i == '*'):
            op_count.add(i)
    cases = list(itertools.permutations(op_count, len(op_count)))
    for c in cases:
        postfix = infix_to_postfix(expression, c)
        result = calculate_postfix(postfix)
        max_ = max(result, max_)
    answer = max_
    return answer



def calculate_postfix(postfix):
    stack = []
    for i in postfix:
        if (i != '+') and (i != '-') and (i != '*'):  # 숫자일 때,
            stack.append(i)
        else:  # 연산자일 때,
            second = int(stack.pop())
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
        if (i != '+') and (i != '-') and (i != '*'):
            num = num + i
        else:
            postfix.append(num)
            while op_stack and case.index(op_stack[-1]) >= case.index(i):
                postfix.append(op_stack.pop())
            op_stack.append(i)
            num = ""
    postfix.append(num)
    while op_stack:
        postfix.append(op_stack.pop())
    ####################################
    return postfix
