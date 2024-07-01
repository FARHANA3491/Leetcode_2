class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
      
        if len(pattern) != len(words):    #if length are not equal, return false
            return False

        #create two dictionary
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern,words):
            if char in char_to_word:
                if char_to_word[char] != word:     #if the pattern and string are different, return false
                    return False
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            if char not in char_to_word and word not in word_to_char:  #If new character, add the value to the 2 dictionaries
                char_to_word[char] = word
                word_to_char[word] = char
        return True       

        
