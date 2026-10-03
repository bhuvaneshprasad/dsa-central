class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            try:
                token = int(token)
            except ValueError:
                pass
            if type(token) == int:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "/":
                    stack.append(int(a / b))
                elif token == "*":
                    stack.append(a * b)
        return stack[0]
