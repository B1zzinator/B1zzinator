def are_parentheses_balanced(origin: str) -> bool:

    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in origin:

        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
          if not stack or stack.pop() != brackets[char]:
                return False


    if len(stack) == 0:
        print("Скобки сбалансированы.")
        return True
    else:
        print("Скобки не сбалансированы.")
        return False
result = are_parentheses_balanced("({[]})")