class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False

        for idx, symbol in enumerate(s):
            if symbol in ["(", "{", "["]:
                stack.append(symbol)
            elif symbol in [")", "}", "]"]:
                if len(stack) < 1:
                    return False
                    
                val = stack.pop()
                if symbol == ")" and val != "(":
                    return False
                if symbol == "}" and val != "{":
                    return False
                if symbol == "]" and val != "[":
                    return False
        
        if len(stack) > 0:
            return False

        return True