class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a in '([{':
                stack.append(a)
            elif a in ')]}':
                if not stack:
                    return False
                top = stack.pop()
                if ((a == ')' and top != '(') or
                    (a == '}' and top != '{') or
                    (a == ']' and top != '[')):
                    return False
        return not stack