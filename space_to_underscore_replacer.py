#!/usr/bin/python3
# -*- coding: UTF-8 -*-

""" space_to_underscore_replacer 1.0
Alfred Workflow Python script that replaces spaces with underscores in the entered text.
"""

import json
import sys

# Grab the query with the entered text
original_text = sys.argv[1]

# Merge multiple lines into a single one
single_line_text = ' '.join(original_text.splitlines())

# Replace spaces with underscores
processed_text = single_line_text.replace(' ', '_')

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
