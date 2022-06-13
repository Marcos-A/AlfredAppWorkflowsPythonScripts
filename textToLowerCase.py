#!/usr/bin/python3
# -*- coding: UTF-8 -*-

""" texToLowerCase 1.0
Alfred Workflow Python script that converts text to lower case.
"""

import json
import sys

# Grab the query with the entered text
originalText = sys.argv[1]

# Convert text to lower case
processedText = originalText.lower()

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
