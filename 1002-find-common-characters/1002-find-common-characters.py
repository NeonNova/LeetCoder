class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # Initialize a dictionary to store the count of each character in the first word
        char_count = {}
        
        # Count the occurrences of characters in the first word
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterate through the remaining words
        for word in words[1:]:
            # Initialize a dictionary to count the occurrences of characters in the current word
            word_count = {}
            
            # Count the occurrences of characters in the current word
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1
            
            # Update char_count to contain the minimum count of each character across all words
            for char in char_count:
                if char in word_count:
                    char_count[char] = min(char_count[char], word_count[char])
                else:
                    char_count[char] = 0
        
        # Initialize an empty list to store the common characters
        result = []
        
        # Iterate through the char_count dictionary
        for char, count in char_count.items():
            # Add each character to the result list the minimum number of times it appears in all words
            result.extend([char] * count)
        
        return result
