# import nltk
# nltk.download() using the GUI 

from nltk import sent_tokenize, word_tokenize

example_text = "Hey! How are you? my name is Aryan. really nice to meet you"

print("general example: " + " ".join(sent_tokenize(example_text))) #observed that it does so mostly by sensing punctuations and spaces 

for i in sent_tokenize(example_text):
    print(i)

#update -- when tokenizing a Unicode string, make sure you are not using an encoded version of the string (it may be necessary to decode it first, e.g. with ``s.decode("utf8")``.

# example -- the example text is modified as follows: 

example_text_modified_byte = b"Hey! How are you? my name is Aryan. really nice to meet you" #this is a byte string

#print(sent_tokenize(example_text)) -- throws an error -- TypeError: cannot use a string pattern on a bytes-like object

decoded_text = example_text_modified_byte.decode("utf8")
print("Decoded example: " + " ".join(sent_tokenize(example_text))) #using .join() as concatenation of str and lists throws an error 
