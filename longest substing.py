def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}  
    start = 0  
    max_len = 0  
    
    for end in range(len(s)):
        current_char = s[end]
        
        if current_char in char_map and char_map[current_char] >= start:
            start = char_map[current_char] + 1
        
        char_map[current_char] = end
        max_len = max(max_len, end - start + 1)
    
    return max_len
s = input("Enter a string:")
result = lengthOfLongestSubstring(s)
print(f"The length of the longest substring without repeating characters is: {result}")
