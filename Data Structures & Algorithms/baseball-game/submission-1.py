class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            print(stack)
            if i == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                a = stack[-1]
                stack.append(2 * a)
            else: 
                stack.append(int(i))
        return sum(stack)