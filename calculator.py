# variable dictionary ----
from collections import deque
variable_dict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def preprocess(args):
    expression = args.split()
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
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
    return expression


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
    postfix = []
    stack = deque()
    for character in expression:
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


def solve_postfix(expression):
    stack = deque()
    for element in expression:
        if element in variable_dict:
            stack.append(variable_dict[element])
        elif element in '+-*/':
            if element == '+':
                if stack:
                    operand1 = stack.pop()
                if stack:
                    operand2 = stack.pop()
                    stack.append(operand1 + operand2)
                else:
                    stack.append(operand1)

            elif element == '-':
                if stack:
                    operand1 = stack.pop()
                if stack:
                    operand2 = stack.pop()
                    stack.append(operand2 - operand1)
                else:
                    stack.append(-1*operand1)
            elif element == '*':
                if stack:
                    operand1 = stack.pop()
                if stack:
                    operand2 = stack.pop()
                stack.append(operand1 * operand2)

            elif element == '/':
                if stack:
                    operand1 = stack.pop()
                if stack:
                    operand2 = stack.pop()
                stack.append(operand2 / operand1)
        else:
            try:
                stack.append(int(element))
            except TypeError:
                print('Unknown Variable')
                return '!'

    return stack.pop()


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
            print(int(result))
