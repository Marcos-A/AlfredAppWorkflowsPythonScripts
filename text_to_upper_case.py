#!/usr/bin/python3
# -*- coding: UTF-8 -*-

""" text_to_upper_case 1.0
Alfred Workflow Python script that converts text to upper case.
"""

import json
import sys

# Grab the query with the entered text
original_text = sys.argv[1]

# Convert text to lower case
processed_text = original_text.upper()

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
