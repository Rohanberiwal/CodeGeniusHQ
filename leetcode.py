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
# leetcode 414 
nums = sorted(list(set(nums)))
        if len(nums) > 2:
            return nums[-3]
        return nums[-1]
#leetcode 378
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
            m = len(matrix)
            n = len(matrix[0])
            list = []
            for i in range(0,m) :
                for j in range(0,n) :
                    list.append(matrix[i][j])
            list.sort()
            return list[k-1]
#leetcode 373 heap  
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pqueue = [(nums1[0] + nums2[0], 0, 0)]
        pairs = []
        while pqueue and len(pairs) < k:
            _, u, v = heapq.heappop(pqueue)
            pairs.append([nums1[u], nums2[v]])
            if v == 0 and u + 1 < len(nums1):
                heapq.heappush(pqueue, (nums1[u+1] + nums2[v], u + 1, v))
            if v + 1 < len(nums2):
                heapq.heappush(pqueue, (nums1[u] + nums2[v+1], u, v + 1))
        return pairs 
# greatest common divisor of the substring
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n,m = len(str1), len(str2)
        if str1 == str2:
            return str1

        if m > n:
            str1, str2 = str2, str1
            n,m = m,n
        
        if str1.startswith(str2):
            return self.gcdOfStrings(str1[m:], str2)
        
        return ""
# leetcode 1952 
class Solution:
    def isThree(self, n: int) -> bool:
        listnew = []
        for i in  range(1,n+1) :
            if n%i==0 :
                listnew.append(i)
        if len(listnew)==3 :
            return True 
        else : 
            return False 
# gcd of max and min array 
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        max = nums[len(nums)-1]
        min = nums[0] 
        return gcd(min,max)
# temperature conversion 

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        listtemp = []
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        listtemp.append(Kelvin)
        listtemp.append(Fahrenheit)
        return listtemp 
# leetcode 65 valid number 
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            if "inf" in s.lower() or "nan" in s.lower():
                return False
            return True
        except:
            return False
        

