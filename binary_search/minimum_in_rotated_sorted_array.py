class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            #Final sorted portion
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
                
            #left sorted portion
            if nums[mid] >= nums[l]:
                res = min(res, nums[l])
                l = mid + 1
                
            #right sorted portion
            else:
                res = min(res, nums[mid])
                r = mid - 1
                
        return res
    
    #Complexity O(logn)
    #Brute O(n)