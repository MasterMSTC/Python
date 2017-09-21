

import urllib
import random

# Load the data from remote location (URL)
file = urllib.request.urlopen(
    "https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")
f = file.read()

# Transform the bitstream into strings
text = f.decode(encoding='utf-8', errors='ignore')

NNNN
