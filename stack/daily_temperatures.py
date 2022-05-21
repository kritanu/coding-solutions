class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_index, stack_temp = stack.pop()
                res[stack_index] = (i - stack_index)
            stack.append([i, t])
        return res
    
    #Complexity O(n), space O(n)
    #Brute O(n^2)