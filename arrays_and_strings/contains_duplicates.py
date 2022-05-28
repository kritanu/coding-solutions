class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            s.add(num)
        if(len(nums) == len(s)):
            return False
        return True
        
        #Complexity O(n)

        #Use sort for O(nlogn)
        #Bruteforce O(n^2)