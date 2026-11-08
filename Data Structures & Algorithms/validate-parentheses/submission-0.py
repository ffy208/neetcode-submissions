class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping:
                stack_top = stack.pop() if stack else "#"
                if stack_top != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
        