class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { ')' : '(', ']' : '[', '}' : '{'}
        
        for parentheses in s:
            if parentheses in hashmap:
                if stack and stack[-1] == hashmap[parentheses]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(parentheses)

        return True if not stack else False

        #Compexity O(n)