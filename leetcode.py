# leetcode 3 sum 15 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        int sum 
        list =[] 
        int size = nums.length() 
        for i in range(size):
            for j in range(i+1 , size):
                for k in range(j+1 ,size) :
                    list[0] =0 
                    list[1]= 0 
                    list[2] = 0;
                    sum  = 0 ;
                    sum = nums[i]+nums[j]+ nums[k]  :
                    if i!=j & j!=k & k!=i & sum = 0 :
                        list[0] = i  
                        list[1] = j  
                        list[2] = k 
                        return list[] 
