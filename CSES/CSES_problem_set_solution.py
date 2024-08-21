

"""
def func( listextra) :
    listreturn  = []
    for i in listextra :
        listnums = [j for j in i]
        size_counter = len(listnums)
        first_letter  = listnums[0]
        print(first_letter)
        last_letter = listnums[-1]
        total_number =  str(first_letter) + str(size_counter) + str(last_letter)
        print(total_number)
        listreturn.append(total_number)
    return listreturn
        
def main() :
    number = int(input("enter the the number of the words"))
    listextra  = []
    for i in range(number) :
        str_input  = input("enter the word")
        listextra.append(str_input)
    output = func(listextra) 
    print(output)
    print("ends")
    
main()

from collections import Counter
def func(results ,  n) :
    counter  = 0
    for i in range(len(results)):
        if results[i].count(1) >= 2 :
            counter = counter +1 
        else :
            continue 
    return counter
        
        
def main():
    n = int(input().strip())
    
    results = []
    for _ in range(n):
        p, v, t = map(int, input().strip().split())
        results.append([p, v, t])
    
    output =  func(results , n)
    print(output)
main()

def func(result , n): 
    x = 0 
    for i in range(n): 
        vis = set(result[i])
        #print(vis)
        if "+" in  vis :
            x =  x+1 
        if "-" in vis : 
            x = x - 1
    return x 

def main() :
    n  = int(input().strip())
    #print(n)
    result  = []
    for _ in range(n):
        str_input  = str(input())
        result.append(str_input)
    #print(result)
    result_out =  func(result , n)
    print(result_out)
    
main()

from itertools import permutations
def compute(listextra , n):
    listoutput= []
    count =  True
    perms  = permutations(listextra)
    print(perms)
    for i in perms  :
        for j in range(len(i)-1) :
            if abs(i[j]-i[j+1]) == 1:
                flag = False
                break 
            else : 
                flag =  True 
        if flag == True  :
            listoutput =   i
        
    return listoutput
            
    
def main() :
    n =  int(input().strip())
    listextra =  [i for i in range(1,n+1)]
    print(listextra)
    numeric = compute(listextra , n)
    print(numeric)
main() 

def generate_beautiful_permutation(n):
    if n == 1:
        return "1"
    elif n == 2 or n == 3:
        return "NO SOLUTION"

    if n % 2 == 0:
        odds = [i for i in range(1, n + 1) if i % 2 != 0]
        evens = [i for i in range(1, n + 1) if i % 2 == 0]
        permutation = evens + odds
    else:

        odds = [i for i in range(1, n + 1) if i % 2 != 0]
        evens = [i for i in range(1, n + 1) if i % 2 == 0]
        permutation = odds + evens

    return permutation

def main():
    n = int(input().strip())
    result = generate_beautiful_permutation(n)
    
    if result == "NO SOLUTION":
        print(result)
    else:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

import math
def main():
    n = int(input().strip())
    print(n)
    print(math.factorial(n))
    listextra =  [ str(i) for i in str(math.factorial(n))]
    listextra.reverse()
    print(listextra)
    count =  0
    for i in range(len(listextra)-1): 
        if listextra[i]== listextra[i+1] == 0:
            count = count + 1
        else: 
            break
    print(count)
main()

def count_trailing_zeros(n):
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    return count

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    trailing_zeros = count_trailing_zeros(n)
    
    print(trailing_zeros)

if __name__ == "__main__":
    main()
"""
