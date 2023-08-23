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
# leetcode 507 
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        i = 2
        while i * i <= num:
            if num  % i == 0:
                sum = sum + i + num/i
            i += 1
        return (True if sum == num and num!=1 else False)
#leetcode self dividing number 728
 l=[]
        for i in range(left,right+1):
            s = str(i)
            if "0" in s:
                continue
            d = 1
            for j in range(len(s)):
                if i % int(s[j]) != 0:
                    d = 0
                    break
            if d == 1:
                l.append(i)
        return l
#leetcode 2520 
class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        count = 0 
        for i in s : 
            if int(num)%(int(i))==0 :
                count = count +1 
        return count 
# leetcode 2806  // standard algorithm for this 

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
            purchaseAmount = ((purchaseAmount - 5) // 10 ) * 10 + 10
            result = 100 - purchaseAmount
            return result
#lleetcode question number 645
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
                duplicate = 0
                error = 0
                n = len(nums)
                nums = sorted(nums)
                for i in range(len(nums)):
                    if nums[i-1] == nums[i]:
                        duplicate = nums[i]
                        break
                nums = list(set(nums))

                for j in range(1, n+1):
                    if j not in nums:
                        error = j
                        break
                return [duplicate, error]

#leetcode question 692 using inbuilt functions 

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(words)
        counts = Counter(words)
        return [word for word, _ in counts.most_common(k)]

#leetcode question  389 the final diffferance 
arr = list(t)
        for i in range(len(s)):
            arr.remove(s[i])
        return arr[0]
#leetcode dynamic programmign 

 a=1
        b=5
        c=0
        while (5**a)<=n:
            c+=n//b
            a+=1
            b=b*5
        return 
#leetcode hard using the dynamic programming 

class Solution:
    def countDigitOne(self, n: int) -> int:
        ans, div, mul = 0, 10, 1
        while n//mul > 0:
            ans += (n//div*mul) + min(max(n%div - mul + 1, 0), mul)
            div *= 10
            mul *= 10
        return ans
# leetcode number of 1 counter in the digit itervative method 
class Solution:
    def countDigitOne(self, n: int) -> int:
        listnew = []
        combined = []
        count = 0
        for i in range(0,n+1) :
            listnew.append(i)
        for i in listnew :
            s = str(i)
            for i in s  :
                combined.append(i)
        for i in combined :
            if i=="1" :
                count = count +1 
        return count
#leetcode 205 isomorphic string 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))     
#leetcode hard using the dynamic programming 

class Solution:
    def countDigitOne(self, n: int) -> int:
        ans, div, mul = 0, 10, 1
        while n//mul > 0:
            ans += (n//div*mul) + min(max(n%div - mul + 1, 0), mul)
            div *= 10
            mul *= 10
        return ans
# leetcode number of 1 counter in the digit itervative method 
class Solution:
    def countDigitOne(self, n: int) -> int:
        listnew = []
        combined = []
        count = 0
        for i in range(0,n+1) :
            listnew.append(i)
        for i in listnew :
            s = str(i)
            for i in s  :
                combined.append(i)
        for i in combined :
            if i=="1" :
                count = count +1 
        return count
#leetcode 205 isomorphic string 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))     
