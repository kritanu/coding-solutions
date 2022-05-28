class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for x, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], x]
            else:
                hashmap[num] = x
        return False

        #Complexity O(n)

        #Bruteforce O(n^2)