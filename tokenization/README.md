
# NLTK tokenizer example

****  This Python code demonstrates how to use the  (NLTK) Natural Language Toolkit's word_tokenizer() and sent_tokenizer() methods to tokenize sentences from a given text string.


## Requirements

Python 3.x (recommended) or higher  
NLTK library (pip install nltk)  
nltk.download() using the GUI -- (just once in the beginning)


## Installation

Install NLTK:

```bash
 pip install nltk
```

#### Download NLTK Resources (First Time Only):
#### Option 1: Using the GUI

Uncomment the line 
```bash 
#nltk.download() in the code.
```
Run the script. It will open a graphical interface where you can download the necessary resources. Select the resources you need (e.g., Punkt Sentence Tokenizer) and click "Download."
it's done when they all turn green.

#### Option 2: Using the Command Line (Optional)

You can download specific resources directly using the command line:

```bash
python -m nltk.downloader Punkt
```

Replace 'Punkt' with the name of the resource you need.

## Explanation

The code imports the sent_tokenize function from the nltk module for sentence tokenization. It defines an example text string. The sent_tokenize function splits the text into individual sentences based on punctuation and whitespace patterns. The script then iterates through the list of sentences and prints each one.

#### Output

The script will print the following output, demonstrating how the text is divided into individual sentences:

```bash
['Hey! How are you?', 'my name is Aryan.', 'really nice to meet you']

```

    
