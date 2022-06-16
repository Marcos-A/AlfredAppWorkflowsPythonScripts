#!/usr/bin/python3
# -*- coding: UTF-8 -*-

""" text_to_music_folder_format 1.0
Alfred Workflow Python script that formats text as music folder
names following the pattern "Artist_Name - Album_Name_(year)"
"""

import json
import sys
import re

# Grab the query with the entered text
original_text = sys.argv[1]

# Capitalize every word
processed_text = ' '.join([word.capitalize() for word in original_text.split(' ')])
# Replace spaces with undescores
processed_text = processed_text.replace(" ", "_")
# Format the dash separating the artist and the album
dash_without_spaces = re.search("[A-Za-z0-9]+-[A-Za-z0-9]+", processed_text)
if dash_without_spaces:
    processed_text = processed_text.replace("-", " - ")
else:
    processed_text = processed_text.replace("_-_", " - ")
# Format the year of release
release_year_without_parenthesis = re.search("[A-Za-z0-9_,.]+\s[-]\s[A-Za-z_,.]+[_][0-9]{4}$", processed_text)
if release_year_without_parenthesis:
    release_year = "(" + re.search("[0-9]{4}$", processed_text).group(0) + ")"
    processed_text = re.sub("[0-9]{4}$", release_year, processed_text)

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
