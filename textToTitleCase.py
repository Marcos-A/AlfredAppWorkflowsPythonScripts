#!/usr/bin/python3
# -*- coding: UTF-8 -*-

""" texToTitleCase 1.0
Alfred Workflow Python script that capitalizes every word in a string.
First letter after a non-alphabet letter is not capitalized.
"""

import json
import sys

# Grab the query with the entered text
originalText = sys.argv[1]

# Capitalize every word
processedText = ' '.join([word.capitalize() for word in originalText.split(' ')])

# Alfred's JSON expected result
processedTextJson = {"items": [
    {
        "type": "file",
        "title": processedText,
        "subtitle": "Copied to clipboard",
        "arg": processedText
    }

]}

# Convert the JSON scheme to string
processedTextJsonString = json.dumps(processedTextJson)

# Pass the resulting JSON string to Alfred
print processedTextJsonString
