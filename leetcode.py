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
#leetcode 205 isomorphic string  ;

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))     
#list comprehension in 118
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [
            [math.comb(i, k) for k in range(i + 1)]
            for i in range(numRows)
        ]
#list comprehension in 118
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [
            [math.comb(i, k) for k in range(i + 1)]
            for i in range(numRows)
        ]

# leetcode 1200 
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = 0
        actual = []
        listfordiff = []
        size = len(arr)
        for i in range(size) :
            for j in range(i+1,size) :
                if arr[j]-arr[i] >mindiff :
                    mindiff = arr[j] - arr[j]

        for i in range(0,size) :
            listfordiff = []
            for j in range(i+1,size) :
                if arr[j]-arr[i] == mindiff  :
                    listfordiff.append(arr[i])
                    listfordiff.append(arr[j])
            if listfordiff==[] :
                continue 
            else :
                actual.append(listfordiff)
        return actual 
# leetcode 1200
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l = len(arr)
        arr.sort()
        answer = [[arr[0], arr[1]]]
        difference = arr[1]-arr[0]
        for i in range(2, l):
            if arr[i] - arr[i-1]==difference: answer.append([arr[i-1], arr[i]])
            elif arr[i] - arr[i-1]<difference: 
                answer = [[arr[i-1], arr[i]]]
                difference = arr[i] - arr[i-1]
        return answer
#leetcode 120 error in the test case 13 have to fix that
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        total = 0
        size =  len(triangle)
        for i in range(0,size-1)  :
            a  = triangle[i+1][i]
            b = triangle[i][i] 
            if(a>b) :
                total  = total + triangle[i][i] 
            else :
                total  = total + triangle[i+1][i]
        return total
#leetcode alternative for the unique binary string 
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        listone = []
        for i in nums :
            d  = int(i,2)
            listone.append(i)
        maxi  = int(max(listone))
        mini  = int(min(listone))
        listbin = []
        for i in range(mini , maxi) :
            binary_string = bin(i)[2:]
            listbin.append(binary_string)
        set1 = set(listbin)
        set2  = set(nums) 
        liste = list(set1.intersection(set2))
        j =  liste[-1]
        return j 
#axctual soluton from teh refracne 
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            binarynums = nums[i][i]
            if binarynums == '1':
                res.append('0')
            else:
                res.append('1')
        return "".join(res)
#leetcode 459 
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool :
        return s in (s + s)[1:-1]
#error on ADD digits leetcode 258 

class Solution:
    def addDigits(self, num: int) -> int:
        listx =  []
        listspare  = []
        sum = 0
        while(num!=0) :
            sum = 0
            r  = num%10
            listx.append(r)
            if(num==0 & len(listx)==1) :
                num  = sum(listx)
                listx =[]
            else  :
                num =  num//10
            
            
        return sum(listx)    
#leetcode add the number of 1 bits 
class Solution:
    def hammingWeight(self, n: int) -> int:
          return list(str(bin(n))).count("1")
#leetcode reverse a bit 
  return int((("{0:032b}".format(n))[::-1]),2)
#leetcode 2119
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        word  = str(num)
        word = word[::-1]
        print(word)
        s  = int(word)
        print(s)
        reverse  = str(s)
        reverse  = reverse[::-1]
        print(reverse)
        return int(reverse) == num
#leetcode intersection of two arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        
        res = []
        for key in c1:
            if key in c2:
                res+= [key]*(min(c1[key],c2[key]))
        return res
#leetcode fizzbuzz 
lass Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        listnew = []
        for i in range(1,n+1):
            if  i%3 ==0 and i%5==0:
                listnew.append("FizzBuzz")
            elif i%3==0 and i%5!=0:
                listnew.append("Fizz")
            elif i%5==0 and i%3!=0:
                listnew.append("Buzz")
            else :
                listnew.append(str(i))
        return listnew

#leetcode 2525
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        word = ""
        flag_1 = False
        flag_2  = False
        vol  = length*width*height
        if length>=10**4 or width >= 10**4 or height >= 10**4 or mass  >= 10**4 or vol >= 10**9 :
           flag_1  = True
        if mass >=100  :
           flag_2  = True 
        if flag_1 == True and flag_2 == True :
            word = "Both"
        elif flag_1 !=True and flag_2 != True  :
            word = "Neither"
        elif flag_1 == True and flag_2 !=True :
            word  ="Bulky"
        else :
            word  = "Heavy"
        return word 
                  


#leetcode 
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
            output = 0
            for i in suits:
                if i != suits[0]:
                    output = 1
            if output == 0:
                return("Flush")

            for j in ranks:
                if ranks.count(j) >= 3:
                    return("Three of a Kind")

            for k in ranks:
                if ranks.count(k) == 2: return("Pair")

            return("High Card") 
#leetcode 434 
class Solution:
    def countSegments(self, s: str) -> int:
#number to hexadecimal  number 
class Solution:
    def toHex(self, num: int) -> str:
        if num<0: num+=2**32
        ans=("%x"% num)
        return ans
#leetcode 338 

class Solution:
    def countBits(self, n: int) -> List[int]:
        listx  =[]
        for i in range(0,n+1):
            binary_num =  bin(i)
            listx.append(str(binary_num))
        binarylist = []
        for i in listx  :
            count = 0
            for j in i :
                if j == "1":
                    count =  count +1 
            binarylist.append(count)
        return binarylist
#leetc code bit wise numebr complement 
class Solution:
    def findComplement(self, num: int) -> int:
        nums  = str(bin(num))
        listx= []
        print(nums)
        for i in nums :
            listx.append(i)
        for i in listx: 
            if i=="1" :
                i ="0" 
            elif i=="0" :
                i  = "1"
        s = "".join(listx)
        print(s)
        return int(s,2)
#leetcode assign cookies 455

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        size   = len(g)
        size2  = len(s)
        count = 0
        if(size>size2) :
            for i in s :
                if i in  g:
                    count  = count +1
                else :
                    continue 
        else :
            for i in g  :
                if i in s :
                    count =  count +1 
        return count  

#sorting algoriihtm for 455 
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            g.sort()
            s.sort()
            i,j=0,0
            tot=0
            while(i<len(g) and j<len(s)):
                if s[j]>=g[i]:
                    i+=1
                    tot+=1
                j+=1
            return tot 
#base 7 question with numpy 
import numpy as np
class Solution:
    def convertToBase7(self, num: int) -> str:
            return np.base_repr(num, base=7)
#leetcode 506
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
            nums =[]
            for i in score :
                nums.append(i)
            listvacent = []
            score.sort(reverse = True) 
            print(nums)
            for i in nums :
                if i == score[0] :
                    listvacent.append("Gold Medal")
                elif i == score[1] :
                    listvacent.append("Silver Medal")
                elif i == score[2] :
                    listvacent.append("Bronze Medal")
                else:
                    listvacent.append(str(score.index(i)+1))
            return listvacent
#leetcode number of bits using power function 

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return str(bin(x^y)).count('1')
#leetcode maximum duplacite remover 229

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size  =int( len(nums) /3)
        listvac= []
        for i in nums :
            if nums.count(i) > size and i not in listvac:
                listvac.append(i)
            else :
                continue
        return listvac
#leetcode 2404
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        size =  len(nums)
        listindex = []
        listx = []
        for i in nums :
            if(i%2==0) :
                listx.append(i)
        for i in listx  :
            listindex.append(count(i)) 
        maxium =0
        for i in listindex  :
            if i > maxium :
               maxium =  i
        return listx[maxium]
##leetcdoe lambda function 
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(x for x in nums if x&1 == 0)
        return min(freq, key=lambda x: (-freq[x], x), default=-1)
#leetcode 646 doubt
import numpy as np
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort() 
        vacent =[]
        for i in pairs :
            vacent.append(i[-1])
        count = 0
        size = len(vacent)
        for i in range(1, len(ar)):
            if ar[i-1] >= ar[i]:
                continue
            else:
                return False            


#leetcode 2248 not with the accurate order 

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        listx=[]
        set1  = set(nums[0])
        for i in nums :
            listx.append(set(i))
        size =  len(listx)
        #for i in range(1,size-1) :
        u = set.intersection(*listx)
        return u  

#leetcode 2248 
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        listx=[]
        set1  = set(nums[0])
        for i in nums :
            listx.append(set(i))
        size =  len(listx)
        u = sorted(set.intersection(*listx))
        return u  
#leetcode 160 Intersection of two linked list Time limit excedded errror at 35/39

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            while headA is not None:
                pB = headB
                while pB is not None:
                    if headA == pB:
                        return headA
                    pB = pB.next
                headA = headA.next
    
            return None
#1523 Tle 72/84
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        while(low!=high+1):
            if low%2 != 0 :
                count = count +1 
            low = low +1 
        return count 
#one liner using the mathemaics 

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low%2 or high%2)
#leetcode 2376 Work on this 
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            word = str(i)
            for i in word  :
                if (int)word.counter(int(i)) >1 :
                   break 
                else:
                    count = count +1
        return count  
# leetcode 500 using the  all keyword in the keyword questions 

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1="qwertyuiop"
        s2="asdfghjkl"
        s3="zxcvbnm"
        arr=[]
        for i in words:
            if all(c in s1 for c in i.lower()) or all(c in s2 for c in i.lower()) or all(c in s3 for c in i.lower()):
               arr.append(i)

        return arr
        





                
