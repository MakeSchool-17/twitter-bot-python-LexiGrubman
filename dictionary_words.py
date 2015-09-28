# read the text file
# select a random set of words from the file
# put those words together in a sentence

import random


words = []

input_file = open('Random-Words.txt', 'r')

for line in input_file:
    words.append(line)

random.shuffle(words)
sentence = ""
for i in range(0, 3):
    sentence += words[i][:-1]
    sentence += " "

print(sentence)
