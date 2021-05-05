'''
변환 성공 infix -> postfix (1h6m 걸림 ㅋㅋ)




'''
def solution(expression):
    answer = 0
    print(infix_to_postfix(expression))
    return answer


def priority_op(op):
    if op == '+':
        return 0
    elif op == '-':
        return 1
    elif op == '*':
        return 2


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
            while op_stack and priority_op(op_stack[-1]) >= priority_op(i): # op_stack이 비어있지 않고, 현 연산자보다 우선순위가 높을 때
                postfix.append(op_stack.pop())
            op_stack.append(i)
            num = ""
    postfix.append(num)  # 마지막 피연산자 추가
    postfix.append(op_stack.pop()) # 이얏!! 역시  op_stack에 남아있을줄 알았엉
    ####################################
    return postfix

solution("100-200*300-500+20")