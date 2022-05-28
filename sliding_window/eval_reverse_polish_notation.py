class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] in ["*", "/", "+", "-"]:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+":
                    stack.append(a+b)
                if tokens[i] == "-":
                    stack.append(a-b)
                if tokens[i] == "*":
                    stack.append(a*b)
                if tokens[i] == "/":
                    stack.append(int(a/b))
            else: stack.append(int(tokens[i]))
        return stack[-1]
        
        #Complexity O(n), space O(n)