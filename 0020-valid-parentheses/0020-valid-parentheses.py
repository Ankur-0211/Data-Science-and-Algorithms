class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        close_to_open={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for bracket in s:
            if bracket in close_to_open:

                if not stack:
                    return False
                if stack[-1]==close_to_open[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        if not stack:
            return True
        return False


        