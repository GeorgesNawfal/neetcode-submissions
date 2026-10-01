class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not len(s) % 2 == 0:
            return False
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            elif stack:
                if p == ')' and stack[-1] == '(' or p == '}' and stack[-1] == '{' or p == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True