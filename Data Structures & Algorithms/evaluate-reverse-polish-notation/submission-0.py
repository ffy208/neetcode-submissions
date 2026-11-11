class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                top_h = stack.pop()
                top_l = stack.pop()
                new_top = top_l + top_h
                stack.append(new_top)
            elif token == '-':
                top_h = stack.pop()
                top_l = stack.pop()
                new_top = top_l - top_h
                stack.append(new_top)
            elif token == '*':
                top_h = stack.pop()
                top_l = stack.pop()
                new_top = top_l * top_h
                stack.append(new_top)
            elif token == '/':
                top_h = stack.pop()
                top_l = stack.pop()
                new_top = top_l / top_h
                stack.append(int(new_top))
            else:
                stack.append(int(token))

        return stack[-1]
                
        