stack = list(input())
stack_2 = []
for i in range(len(stack)):
    symb = stack.pop()
    if symb == "}" or symb == ")" or symb == "]":
        stack_2.append(symb)
    else:
        if len(stack_2) == 0:
            print("NO")
            break
        symb_2 = stack_2.pop()
        if symb == "(" and symb_2 != ")":
            print("NO")
            break
        if symb == "{" and symb_2 != "}":
            print("NO")
            break
        if symb == "[" and symb_2 != "]":
            print("NO")
            break
else:
    if len(stack_2) == 0:
        print("YES")
    else:
        print("NO")