'''
postfix 계산까지는 클리엌!
'''
def solution(expression):
    answer = 0
    postfix = infix_to_postfix(expression)
    print(postfix)
    result = calculate_postfix(postfix)
    print(result)
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


def infix_to_postfix(exp):
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
            while op_stack and priority_op(op_stack[-1]) >= priority_op(i):  # op_stack이 비어있지 않고, 현 연산자보다 우선순위가 높을 때
                postfix.append(op_stack.pop())
            op_stack.append(i)
            num = ""
    postfix.append(num)  # 마지막 피연산자 추가
    while op_stack:   # op_staack 빌 때까지 실행한다.
        postfix.append(op_stack.pop())  # 이얏!! 역시  op_stack에 남아있을줄 알았엉
    ####################################
    return postfix

solution("100-200*300-500+20")