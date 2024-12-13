#Reverse Word Order in a String
#Write a Python function that takes a string as input and reverses the order of words in the string without using built-in 
#Python methods like split(). For example, if the input is "Hello World", the output should be "World Hello".

def reverse_word_order(input_string):
    words = []
    word = ""
    for char in input_string:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    if word:
        words.append(word)
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    reversed_string = ""
    for word in reversed_words:
        if reversed_string:
            reversed_string += " "
        reversed_string += word
    return reversed_string

#input
input_str = "This is Lakshman"
output_str = reverse_word_order(input_str)
print(output_str)  # Output: "World Hello"
