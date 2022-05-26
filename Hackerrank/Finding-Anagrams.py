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

