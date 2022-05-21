class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openB, closedB):
            
            if openB == closedB == n:
                res.append("".join(stack))
                return 
            
            if openB < n:
                stack.append("(")
                backtrack(openB + 1, closedB)
                stack.pop()
            if closedB < openB:
                stack.append(")")
                backtrack(openB, closedB + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res
    
    #Complexity O(4^n/root n), space O(n)
    #Brute O(2^2n.n)