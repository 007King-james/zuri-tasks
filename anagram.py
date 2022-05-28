# Check if two words are anagrams
# Example:
# find_anagrams('hello', 'check') --> False
# find_anagrams('below', 'elbow') --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    if(sorted(word) == sorted(anagram)):
        print("True")
    else:
        print("False")

word = "below"
anagram = "elbow"
find_anagram(word, anagram)

    
        
