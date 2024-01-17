# Expression

import sys

def precedence(operator):
    if operator in ("+", "-"):
        return 1
    elif operator in ("*", "/", "%"):
        return 2
    else:
        return 0

def apply_operator(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b
    if op == "%": return a % b

def evaluate(tokens):
    values = []
    ops = []
    i = 0

    while i != len(tokens):
        if tokens[i] == " ":
            i += 1
            continue

        elif tokens[i] == "(":
            ops.append(tokens[i])

        elif tokens[i].isdigit():
            val = 0
            decimal_found = False
            while i != len(tokens) and (tokens[i].isdigit() or tokens[i] == "."):
                if tokens[i] == ".":
                    decimal_found = True
                    dividor = 10
                elif not decimal_found:
                    val = val*10 + int(tokens[i])
                else:
                    val += int(tokens[i]) / dividor
                    dividor *= 10
                i += 1
            values.append(val)
            i -=1

        elif tokens[i] == ")":
            while ops[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_operator(val1, val2, op))
            ops.pop()
            i += 1
        else:
            while len(ops) and precedence(ops[-1]) >= precedence(tokens[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_operator(val1, val2, op))
            ops.append(tokens[i])
        i += 1
        
    while len(ops) != 0: 
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_operator(val1, val2, op))
    
    result = values[0]
    if result == int(result):
        return int(result)
    else:
        return result
    
result = evaluate(sys.argv[1])
print(result)