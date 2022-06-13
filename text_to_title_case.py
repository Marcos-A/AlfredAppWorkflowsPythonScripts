#!/usr/bin/python3
# -*- coding: UTF-8 -*-

""" texToTitleCase 1.0
Alfred Workflow Python script that capitalizes every word in a string.
First letter after a non-alphabet letter is not capitalized.
"""

import json
import sys

# Grab the query with the entered text
original_text = sys.argv[1]

# Capitalize every word
processed_text = ' '.join([word.capitalize() for word in original_text.split(' ')])

# Alfred's JSON expected result
processed_text_json = {"items":
                        [
                            {
                             "type": "file",
                             "title": processed_text,
                             "subtitle": "Copied to clipboard",
                             "arg": processed_text
                            }
                        ]
                      }

# Convert the JSON scheme to string
processed_text_json_string = json.dumps(processed_text_json)

# Pass the resulting JSON string to Alfred
print(processed_text_json_string)
