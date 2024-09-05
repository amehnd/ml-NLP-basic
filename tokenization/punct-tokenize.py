from nltk import sent_tokenize, word_tokenize
example_text = "Hey! How are you? my name is Aryan. really nice to meet you"

print(sent_tokenize(example_text)) 

for token in wordpunct_tokenize(example_text):
    print(token, end=" $ ") #using '$' to differentiate between tokens

