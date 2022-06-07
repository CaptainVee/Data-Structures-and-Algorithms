'''
Question 4
Given an integer n, your task is to count how many strings of length n can be 
formed under the following rules:

    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7. 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3: 

Input: n = 5
Output: 68

 Constraints:

    1 <= n <= 2 * 10^4

'''
import time
import itertools
def countVowelPermutation(n):
    start = time.time()
    vowel = ['a', 'e', 'i', 'o', 'u']
    result = itertools.product(vowel, repeat=n)
    big_list = []
    c = 0
    for i in result:
        print(i)
        c+=1
        
        sub = []
        sub.append(i[0])
        for j in range(1, len(i)):
            try:
                if i[j] == 'a':
                    if sub[-1] in ['a', 'o']:
#                        sub.append(i[j])
                        break
                
                elif i[j] == 'e':
                    if sub[-1] in ['e', 'o', 'u']:
#                        sub.append(i[j])
                        break
                        
                elif i[j] == 'i':
                    if sub[-1] in ['a','i', 'u']:
#                        sub.append(i[j])
                        break
                        
                elif i[j] == 'o':
                    if sub[-1] in ['a','e', 'o', 'u']:
#                        sub.append(i[j])
                        break
                
                elif i[j] == 'u':
                    if sub[-1] in ['a', 'e', 'u']:
#                        sub.append(i[j])
                        break
                sub.append(i[j])
            except IndexError:
                pass
        if len(sub) == len(i):
            big_list.append(sub)
    
    end = time.time()
    print("The time of execution of above program is :", end-start)
    return len(big_list), c
        
countVowelPermutation(5) 
