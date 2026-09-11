class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "*" or token == "-" or token == "/":
                f = int(stack.pop())
                s = int(stack.pop())

                if token == "+":
                    stack.append(int(f + s))

                if token == "-":
                    stack.append(int(s - f))

                if token == "*":
                    stack.append(int(f * s))

                if token == "/":
                    stack.append(int(s / f))
            
            else:
                stack.append(int(token))
        
        return stack[0]

        