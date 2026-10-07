class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        paren= {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in paren:
                if stack and stack[-1] == paren[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

        