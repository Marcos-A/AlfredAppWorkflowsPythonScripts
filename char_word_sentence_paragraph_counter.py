#!/usr/bin/python3
# -*- coding: UTF-8 -*-

""" word_sentence_paragraph_counter 1.0
Alfred Workflow Python script that counts the number of
words, sentences and paragraphs in a given text.
"""

import json
import sys
import re

# Grab the query with the entered text and remove leading and trailing spaces
text_str = sys.argv[1].strip()

# Obtain total number of characters
chars_count = len(text_str)

# Prepare response
if chars_count == 1:
    chars_count_response = str(chars_count) + " character"
else:
    chars_count_response = str(chars_count) + " characters"


# Separate words and add them to list
words_list = text_str.split()

# Obtain total number of words in words list
words_count = len(words_list)

# Prepare response
if words_count == 1:
    words_count_response = str(words_count) + " word"
else:
    words_count_response = str(words_count) + " words"


# Replace question and exclamation marks with dots
no_questions_text = text_str.replace("?", ".")
no_exclamations_nor_questions_text = no_questions_text.replace("!", ".")

# Remove duplicated dots
clean_dots_text = re.sub(r'(\.\.)\.*|\.', r'.', no_exclamations_nor_questions_text)

# Separate sentences and add them to list
sentences_list = clean_dots_text.split(".")

# Obtain total number of sentences in sentences list
# A sentence without a final dot is still considered a sentence
if clean_dots_text.endswith("."):
    sentences_count = len(sentences_list)-1
else:
    sentences_count = len(sentences_list)

# Prepare response
if sentences_count == 1:
    sentences_count_response = str(sentences_count) + " sentence"
else:
    sentences_count_response = str(sentences_count) + " sentences"


# Remove leading, trailing and duplicated line breaks
clean_line_breaks_text = re.sub(r'(\n\n)\n*|\n', r'\n', text_str.strip('\n'))

# Separate paragraphs and add them to list
paragraph_list = clean_line_breaks_text.split("\n")

# Obtain total number of paragraphs in paragraphs list
paragraph_count = len(paragraph_list)

# Prepare response
if paragraph_count == 1:
    paragraph_count_response = str(paragraph_count) + " paragraph"
else:
    paragraph_count_response = str(paragraph_count) + " paragraphs"


# Prepare response
words_sentences_paragraphs_count = chars_count_response +\
                                   " · " +\
                                   words_count_response +\
                                   " · " +\
                                   sentences_count_response +\
                                   " · " +\
                                   paragraph_count_response

# Alfred's JSON expected result
words_sentences_paragraphs_count_json = {"items":
                                            [
                                                {
                                                 "type": "file",
                                                 "title": words_sentences_paragraphs_count,
                                                 "subtitle": "Copied to clipboard",
                                                 "arg": words_sentences_paragraphs_count
                                                }
                                            ]
                                          }

# Convert the JSON scheme to string
words_sentences_paragraphs_count_json_string = json.dumps(words_sentences_paragraphs_count_json)

# Pass the resulting JSON string to Alfred
print(words_sentences_paragraphs_count_json_string)
