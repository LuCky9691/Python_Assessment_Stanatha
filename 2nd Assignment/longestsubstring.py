#Longest Substring Without Repeating Characters
#Write a Python program to find the length of the longest substring without repeating characters. 
#For example, for the input string "abcabcbb", the program should return 3 (substring "abc").


def length_of_longest_substring(s):
    char_index = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# input
input_string = "abcdefghiabcbb"
result = length_of_longest_substring(input_string)
print(result)  # Output: 3
