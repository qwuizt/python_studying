import re
from collections import Counter

text = """
    Python 3.11.5 documentation
Welcome! This is the official documentation for Python 3.11.5.

Parts of the documentation:

What's new in Python 3.11?
or all "What's new" documents since 2.0

Tutorial
start here

Library Reference
keep this under your pillow

Language Reference
describes syntax and language elements

Python Setup and Usage
how to use Python on different platforms

Python HOWTOs
in-depth documents on specific topics

Installing Python Modules
installing from the Python Package Index & other sources

Distributing Python Modules
publishing modules for installation by others

Extending and Embedding
tutorial for C/C++ programmers

Python/C API
reference for C/C++ programmers

FAQs
frequently asked questions (with answers!)

Indices and tables:

Global Module Index
quick access to all modules

General Index
all functions, classes, terms

Glossary
the most important terms explained

Search page
search this documentation

Complete Table of Contents
lists all sections and subsections

Meta information:

Reporting bugs

Contributing to Docs

About the documentation

History and License of Python

Copyright
    """

text = re.sub(r'[^\w\s]', ' ', text).lower()

words = text.split()
word_count = Counter(words)
most_common_words = word_count.most_common(10)

for word, count in most_common_words:
    print(f"{word}: {count}")
