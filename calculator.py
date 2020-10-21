# variable dictionary ----
from collections import deque
variable_dict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def preprocess(args):
    # print(args)
    expression = args.split()
    # print(expression)
    for i in range(len(expression)):
        if len(expression[i]) > 1:
            if expression[i][0] == '+' and expression[i][1] == '+':
                expression[i] = '+'
            if expression[i][0] == '-' and expression[i][1] == '-':
                if len(expression[i])%2 == 0:
                    expression[i] = '+'
                else:
                    expression[i] = '-'
    expression = ''.join(expression)
    # print(expression)
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
    # print(expression)
    return expression
# preprocess('-10')



def identifier_check(arg):
    for character in arg:
        if character not in alphabet:
            print('Invalid identifier')
            return False
    return True


def command_handler(args):
    if args == '/help':
        print('Its a calculator')
    elif args == '/exit':
        print('Bye!')
        exit()
    else:
        print('Unknown Command')


def assignment_handler(args):
    args = args.split('=')
    args = [arg.strip() for arg in args]
    if len(args) > 2:
        print('Invalid assignment')
    else:
        if identifier_check(args[0]):
            try:
                variable_dict[args[0]] = int(args[1])
            except (TypeError, ValueError):
                if not identifier_check(args[1]):
                    print('Invalid assignment')
                else:
                    try:
                        variable_dict[args[0]] = variable_dict[args[1]]
                    except KeyError:
                        print('Unknown variable')


def infix_to_postfix(expression):
    # print('Infix: ', expression)
    postfix = []
    stack = deque()
    # print(expression)
    for character in expression:
        # print(character)
        if character in '*/(':
            stack.append(character)
        elif character == ')':
            while True:
                if stack:
                    popped_operator = stack.pop()
                    if popped_operator == '(':
                        break
                    else:
                        postfix.append(popped_operator)
                else:
                    print('Invalid Expression')
                    return 0
        elif character in '+-':
            while True:
                if stack:
                    popped_operator = stack.pop()
                    if popped_operator in '+-*/':
                        postfix.append(popped_operator)
                    if popped_operator == '(':
                        stack.append(popped_operator)
                        break
                else:
                    break
            stack.append(character)
        else:
            postfix.append(character)
    while True:
        if stack:
            postfix.append(stack.pop())
        else:
            break
    if '(' in postfix:
        print('Invalid Expression')
        return 0
    return postfix
    # print(postfix)

# infix_to_postfix(['8', '*', '3', '+', '12', '*', '(', '4', '-', '2', ')'])




def solve_postfix(expression):
    stack1 = deque()
    # stack2 = deque()
    # print('Postfix: ', expression)
    for element in expression:
        if element in variable_dict:
            stack1.append(variable_dict[element])
        elif element in '+-*/':
            if element == '+':
                if stack1:
                    operand1 = stack1.pop()
                if stack1:
                    operand2 = stack1.pop()
                    stack1.append(operand1 + operand2)
                else:
                    stack1.append(operand1)

            elif element == '-':
                if stack1:
                    operand1 = stack1.pop()
                if stack1:
                    operand2 = stack1.pop()
                    stack1.append(operand2 - operand1)
                else:
                    stack1.append(-1*operand1)
            elif element == '*':
                if stack1:
                    operand1 = stack1.pop()
                if stack1:
                    operand2 = stack1.pop()
                stack1.append(operand1 * operand2)

            elif element == '/':
                if stack1:
                    operand1 = stack1.pop()
                if stack1:
                    operand2 = stack1.pop()
                stack1.append(operand2 / operand1)
        else:
            try:
                stack1.append(int(element))
            except:
                print('Unknown Variable')
                return '!'

    return stack1.pop()

# solve_postfix(['8', '3', '*', '12', '4', '2', '-', '*', '+'])
# def calculator(args):
#     pass
    # expression = args.replace('+', '').replace('--', '').replace('-', ' - ').replace('(', ' ( ').replace(')', ' ) ').split()
    # modified_expression = []
    # for i in range(len(expression)-1):
    #     if expression[i] in '+-*/()' or expression[i+1] in '+-*/()':
    #         modified_expression.append(expression[i])
    #     else:
    #         modified_expression.append(expression[i])
    #         modified_expression.append('+')
    # modified_expression.append(expression[-1])
    #
    # print(modified_expression)

    # total = 0
    # flag = 0
    # arg = ''
    # try:
    #     for number in numbers:
    #         arg = number
    #         if number == '+':
    #             continue
    #         if number == '-':
    #             flag = 1
    #             continue
    #         if flag == 1:
    #             if number[0] in alphabet:
    #                 total -= variable_dict[number]
    #             else:
    #                 total -= int(number)
    #             flag = 0
    #         else:
    #             if number[0] in alphabet:
    #                 total += variable_dict[number]
    #             else:
    #                 total += int(number)
    #     print(total)
    # except KeyError:
    #     if identifier_check(arg):
    #         print('Unknown Variable')


while True:
    arguments = input()
    if len(arguments) == 0:
        continue
    if arguments[0] == '/':
        command_handler(arguments)
        continue
    if '=' in arguments:
        assignment_handler(arguments)
        continue
    if '**' in arguments or '//' in arguments:
        print('Invalid expression')
        continue
    arguments = preprocess(arguments)
    postfix = infix_to_postfix(arguments)
    if postfix:
        result = solve_postfix(postfix)
        if result != '!':
            print(result)
    # else:
    #     continue
    # print(arguments)
    # print(postfix)

    # calculator(arguments)

