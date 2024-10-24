def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

input_sentence = "Hello world! Hello everyone. Welcome to the world."
result = word_frequency(input_sentence)
print(result)
