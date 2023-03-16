# Natural Language Processing with ASametYildirim


What will I learn here?

- Natural language processing basics
- Text and word classification and clustering
- Deep learning in natural language processing

## Natural language processing basics
### What is natural language processing?
It is more developed with natural language processing, linguistics and artificial intelligence and takes place in almost every area of our daily life. Basically, it aims to provide communication between human language and computer.

Natural language processing is the process of evolving raw texts into a format that computers can interpret.



## Historical development of natural language processing
- Alan Turing "Computing Machinery and Intelligence?" He publishes his article and is accepted as the foundation of artificial intelligence.
- He is doing the "Goergetown Experiment" in 1954 and aims to translate 60 words from Russian into English.
- In the 1960s, ELIZA provided communication between humans and machines with the "Rogerian Psychotherapist Simulation".
- Statistical Machine Translations in the 1980s.
- 1980 Used for representational learning and deep learning models.
- 1970 - 19080 Chatbot

### Uses of natural language processing
- Machine Translation
- Speech Recognition
- Sentiment Analysis
- Question Answering

## Subheadings of natural language processing
- Vocabulary
-> Search for the roots of a word in a language
- Syntax
-> Explores sentence construction and flexibility in natural languages
- Semantic Analysis
-> Searches sentence meanings with word meaning
- Ambiguity
-> Searches context with word meaning

## Major research topics of natural language processing
- Entity Name Recognition
1- Custom name

2- date, time, location

3- person institution name

- Summarizing
1- Extractive summarization (Words and sentences in the text)

2- Abstracting summary (Words and sentences that cannot be included in the text)

- Text Normalization
Elimination of typos increases the success rate
- Text Classification
-> Classification of text such as meaning and length

## Core Libraries

### NLTK
- Natural Language Toolkit
- Statistical and symbolic NLP
- Python
- Steven Bird & Edward Loper

### SPACY
- Open source code
- Python and Cpython
- Matthew Honnibal & Ines Montani
- Machine learning and neural networks

### BASIN
- Turkish NLP
- Open Source code
- Java
- Ahmet Afsin & Mehmet Dundar AKIN


## Tokenize
### What is Token?
Tokens are raw sentences, words, punctuation marks, numbers, symbols.

Tokenize a sentence (punctuation)
Tokenize words (spaces and punctuation)

## Trunking - Headword Extraction - Ineffective Words
### Why should we remove stemming and leading words?
For example: It may have taken both a constructive and an inflectional affix, such as flower-lik-ler.

Inferring the meaning of a text is usually done by finding the root. Because the meaning is here.

### hulling
It tries to find the root of the word by removing all construction and inflectional suffixes.


# Word Types
- POS: Part-Of-Speech -> Word Type
- POSTagging -> Marking a Word Type
- Word Types -> Adjective, Object, Predicate, Conjunction etc.
- Purpose -> To mark the word type of each word

## Rule-Based Vocabulary Marking Models
An unknown type X word
- Adjective Rule: Adverb + X + Noun
- -ing Rule: Verb + X (finished with -ing)
- Capitalization Rule: X (Started with a capital letter)
