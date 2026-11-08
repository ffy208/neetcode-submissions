class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in mapping:
                if not stack:
                    return False
                
                if stack.pop() != mapping[char]:
                    return False

            else:
                stack.append(char)

        return not stack