class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                break
                
        if not (top <= bottom):
            return False
        
        m = (top + bottom) // 2
        row = matrix[m]
        
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target == row[mid]:
                return True
            elif target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1
        return False
    
    #Complexity logm.logn space O(1)
    #Brute m.log n 