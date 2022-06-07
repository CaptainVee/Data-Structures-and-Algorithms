# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
	a = 0
    for i in word:
    	if i in anagram:
    		a+=1
    if a == len(anagram):
    	return True
    else:
    	return False

'''
We declear a variable a, then we loop through each letter in the first string(word)
and then check if it is in the other string(anagram). If it is there, we increment
our variable a. Then lastly we check if a is equal to the length of the anagram string
'''

