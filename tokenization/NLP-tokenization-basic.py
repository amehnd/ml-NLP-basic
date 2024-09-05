# import nltk
# nltk.download() using the GUI 

from nltk import sent_tokenize, word_tokenize

example_text = "Hey! How are you? my name is Aryan. really nice to meet you"

print(sent_tokenize(example_text)) #observed that it does so mostly by sensing punctuations and spaces 

for i in sent_tokenize(example_text):
    print(i)


