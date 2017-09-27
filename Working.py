

## Python script for MSTC classroom activities


###### Loading Data In Your Python Dictionary

# The data used are the reviews of Donna Tartt’s The Goldfinch in the Amazon book review
# set from the Irivine Machine Learning Repository. These reviews have been stored
# in a simple tab separated file, which is nothing more than a plain text file
# with columns.
#  The table contains four columns:
#            review score, url, review title and review text.

# There are several ways imaginable to put this into a dictionary, but in this case,
#  you take the url as the dictionary keys and put the other columns in the
#  nested values dictionary.


import urllib
import random

# Load the data from remote location (URL)
file = urllib.request.urlopen(
    "https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")
f = file.read()

# Transform the bitstream into strings
text = f.decode(encoding='utf-8', errors='ignore')

