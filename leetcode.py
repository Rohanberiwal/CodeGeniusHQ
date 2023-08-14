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
# leetcode 39 combination sum error ithis only  1 basse case passing 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        klist = []
        newlist = []
        size = len(candidates)
        sum = 0
        for i in range(0,len(candidates)):
            klist = []
            sum  = 0
            for j in range(0,len(candidates)) :
                sum = sum + candidates[i] + candidates[j] 
                if sum==target :
                    klist.append[candidates[j]]
                else :
                    continue 
                newlist.append(klist)
        return newlist 
# leetcode anagram using the inbuilt function 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
# valid palindrome check
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=("".join(i for i in s if i.isalnum())).lower()
        return new==new[::-1]


#leetcode 2210
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hillValley = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:    
                hillValley += 1
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:    
                hillValley += 1
        return hillValley
# code to reverse a strign 151
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        reversed_list = word_list[:: -1]
        reversed_sentence = " ".join(reversed_list)
        return reversed_sentence 
# leetcode mergee intervals mot made by me this one is copied 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                previous_end = merged[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                if previous_end >= current_start: # overlap
                    merged[-1][1] = max(previous_end,current_end)
                else:
                    merged.append(intervals[i])
        return merged
# merge intervals alternativvly 1768
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = "" 
        i = 0
        while (i < len(word1)) or (i < len(word2)):
            if (i < len(word1)):
                result += word1[i]
            if (i < len(word2)):
                result += word2[i] 
                
            i += 1
            
        return result
        
