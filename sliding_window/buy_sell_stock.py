class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer, right_pointer = 0, 1
        profit = 0
        for i in range(len(prices)-1):
            if(prices[right_pointer] > prices[left_pointer]):
                profit = max(prices[right_pointer] - prices[left_pointer], profit)
            elif(prices[right_pointer] <= prices[left_pointer]):
                left_pointer = right_pointer
            else:
                left_pointer += 1
            right_pointer+=1
        return profit