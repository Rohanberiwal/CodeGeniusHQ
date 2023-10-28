class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        totalsum  =  sum(nums)
        
        nums.sort(reverse = True)
        
        numsum = 0 
        extra = []
        for i in nums :
            if numsum <= totalsum  - numsum  :
               extra.append(i)
               numsum = numsum  + i 
            elif numsum > totalsum - numsum  :
                break 
        return extra
            

            

        
