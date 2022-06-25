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
text_str = sys.argv[1]

# Replace undescores with spaces
text_str = text_str.replace("_", " ")

# Add spaces before and after dashes separating artist and album
dash_without_spaces = re.search("[A-Za-zÀ-ÖØ-öø-ÿ0-9_,.\s]+^(_)[-]^(_)[A-Za-zÀ-ÖØ-öø-ÿ0-9_,.()\s]", text_str)
if dash_without_spaces:
    text_str = text_str.replace("-", " - ")

# Capitalize every word
text_str = ' '.join([word.capitalize() for word in text_str.split(' ')])

# Replace spaces with undescores
text_str = text_str.replace(" ", "_")

# Replace slashes with ampersands
text_str = text_str.replace("/", "&")

# Format the dash separating the artist and the album
dash_without_spaces = re.search("A-Za-zÀ-ÖØ-öø-ÿ0-9]+-[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", text_str)
if dash_without_spaces:
    text_str = text_str.replace("-", " - ")
else:
    text_str = text_str.replace("_-_", " - ")

# Format the year of release
release_year_without_parenthesis = re.search("[A-Za-zÀ-ÖØ-öø-ÿ0-9_,.]+\s[-]\s[A-Za-zÀ-ÖØ-öø-ÿ_,.]+[_][0-9]{4}$", text_str)
if release_year_without_parenthesis:
    release_year = "(" + re.search("[0-9]{4}$", text_str).group(0) + ")"
    text_str = re.sub("[0-9]{4}$", release_year, text_str)

# Alfred's JSON expected result
text_str_json = {"items":
                        [
                            {
                             "type": "file",
                             "title": text_str,
                             "subtitle": "Copied to clipboard",
                             "arg": text_str
                            }
                        ]
                      }

# Convert the JSON scheme to string
text_str_json_string = json.dumps(text_str_json)

# Pass the resulting JSON string to Alfred
print(text_str_json_string)
