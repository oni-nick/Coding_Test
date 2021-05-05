def solution(expression):
    answer = 0
    infix_to_postfix(expression)
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
            if not op_stack:    # 빈리스트 처리
                op_stack.append(i)
            elif priority_op(op_stack[-1]) >= priority_op(i):  # 연산자 우선순위 비교, 우선순위 변경 함수 사용함
                print("-----=>",priority_op(op_stack[-1]), priority_op(i), op_stack[-1], i)##########################################################
                if not op_stack: # 빈 리스트인 경우만 아래 32~35 실행, 이러면 안되지
                    while priority_op(op_stack[-1]) >= priority_op(i): # 연산자 우선순위 비교
                        op = op_stack.pop()
                        postfix.append(op)
                        print("실행여부") # 이 부분 실행 안됨
            elif priority_op(op_stack[-1]) < priority_op(i):
                op_stack.append(i)
            num = ""
    postfix.append(num)  # 마지막 피연산자 추가
    ####################################


solution("100-200*300-500+20")