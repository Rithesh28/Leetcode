class Solution(object):
    def isValid(self, s):
        stack=[]
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                last=stack.pop()
                if last == '(' and ch != ')':
                    return False

                if last == '[' and ch != ']':
                    return False

                if last == '{' and ch != '}':
                    return False
        return len(stack) == 0
                
        