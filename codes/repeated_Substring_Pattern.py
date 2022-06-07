
''''
Question 5
Given a string s, check if it can be constructed by taking a substring of it and
 appending multiple copies of the substring together.

 

Example 1:

Input: s = 
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

 

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.


'''

def repeatedSubstringPattern(s):
    substring = []
    occurance = 0
    
    #take half of the sting
    new = s[:len(s)//2]
    
    for each_letter in new:
        substring.append(each_letter)
        
        #change list of string to a single string
        list_to_string = ''.join(substring)
        occurance = s.count(list_to_string)
        
        #we multiply the occurance by the number of string in the occurance to see if it would give the complete string
        if (len(substring)*occurance) == len(s) and occurance >1:
            return True
        
    return False
        
repeatedSubstringPattern('abcabcabcabc') 



