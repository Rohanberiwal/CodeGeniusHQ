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
# leetcode question integer to roman numerals 

class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_numeral = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1
        return roman_numeral
        
# leetcode problem 344 
class Solution(object):
    def reverseString(self, s):
        s = s.reverse()
        return s 
# LEETCODE 65
class Solution:
    def isNumber(self, s: str) -> bool:
        for i in s :
            if s.isdigit() or type(s)==float :
                return True 
            else :
                return False 
