#!/usr/bin/env python3

import os
import re

episodeRegex = re.compile("[0-9][0-9]?.[0-9][0-9]?")

for filename in os.listdir('.'):
	if os.path.isfile(filename):
		# Check if string contains something like S01E01.
		# If so, it's probably a tv show.
		try:
			episodeNumber = episodeRegex.findall(filename)[0]
			episodeNumber = "S" + episodeNumber[:1] + "E" + episodeNumber[3:]
		except IndexError:
			episodeNumber = "delete"
		nameStarter = "AdventureTime_" # Replace this with the name of the show.
		filetype = filename[-4:] 
		newName = nameStarter + episodeNumber + filetype
		os.rename(filename, newName)
