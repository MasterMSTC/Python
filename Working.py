

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

# Initalising the dictionary
reviews = {}

# Filling the dictionary
for line in lines:
    l = line.strip().split("\t")

    # These are just training wheels to see more clearly what goes into the dictionary
    score = l[0]
    id = l[1]
    title = l[2]
    review = l[3]

    # NOTICE: each dict entry is also a DICT !!

    reviews[id] = {"score": score, "title": title, "review": review}
    
    ###### How To Filter a Dictionary in Python

# Let’s say you are interested in the bad reviews and want to see what people
#  actually wrote by selecting only the reviews that score 1.0


# Python dictionary items not only have both a key and a value, but they also have a
# special iterator to loop over them. Instead of for item in dictionary, you need to
# use for key, value in dictionary.items()

# Store review keys with low score (1.0) in list
lowscores = []
for key, value in reviews.items():
    if float(value["score"]) == 1.0:  # Convert score to float
        lowscores.append(key)

# Print all the entries with a low review score
for item in lowscores:
    print(reviews[item])

    ###### Python Dictionary Operations

    # EXTRACTING a subset
    # you use the keys stored in lowscores to create the new dictionary.
    #  There are two options for this: one just retrieves the relevant items
    # from the original dictionary with the .get() method leaving the original
    # intact, the other uses .pop() which does remove it permanently from the original dictionary.

    # for-loop style to subset a dictionary
    forloop = {}
    for k in lowscores:
        forloop[k] = reviews[k]

    # List comprehension to get a subset dictionary.
    # Alternatively you can use `.pop` instead of `.get`
    dictcomp = {k: reviews.get(k) for k in lowscores}

    # Verify that these objects are equal
    print(forloop == dictcomp)

    from collections import defaultdict

###### How To Sort Dictionaries in Python

### Very simple NLP frequency of words in bad reviews
# If you are interested in the words that go hand in hand with a negative sentiment
#  about the novel,
#  you could do a low-level form of sentiment analysis by making a frequency list
# of the words in the
# negative reviews (scored 1.0).

# Regular Expressions
# You need to process the review text a little bit by removing the HTML-tags
#  and converting uppercase words
# to lowercase.
#
# For the first we use a regular expression which removes
# all tags: re.sub("<.*?>", "").

# defaultdict
# you build the frequency dictionary using a defaultdict instead
#  of a normal dictionary.
# This guarantees that each “key” is already intialized and
#  you can just increase the frequency count with 1.

# If you were not using defaultdict, Python would raise an error
#  when you try to increase the count for the
# first time (so from 0 to 1) because the key does not yet exist.

import re
# Import defaultdict
from collections import defaultdict

freqdict = defaultdict(int)  # default value of int is 0
for item in lowscores:
    review = reviews[item]["review"]
    cleantext = re.sub(r'<.*?>', '',
                       review).strip().split()  # Remove HTML tags and split the review by word (space separated)
    for word in cleantext:
        # Convert to all lowercase
        word = word.lower()

        # Complete the following line to increase the count by one:
        freqdict[word] += 1

print(freqdict)

# Once the frequency dictionary is ready, you still need to sort the keys by value
#  in descending order to
#  see promptly which words are highly frequent.
#  As normal dictionaries (including defaultdict can not be ordered by design)
# , you need another class,
#  namely OrderedDict.

### The sorted function takes 3 arguments.

# FIRST: The first one is the object that you want to sort, your
# frequency dictionary. Remember however that accessing the key-value
# pairs in a dictionary is only possible through the .items() function!

# SECOND
# the second argument specifies what part of the first argument should
#  be used to sort: key=lambda item: item[1]
#  lambda function is an anonymous function,
# meaning it is a function without a name and can not be called from outside.
# In this case, it simply uses
# the dictionary value (item[1], with item[0] being the key)
#  as the argument for sorting.


# THIRD
# The third and final argument, reverse, specifies whether sorting should be
#  ascending (the default) or descending.
# In this case, you want to see the most frequent words at the top
# and need to specify explicitly that reverse=True.

from collections import OrderedDict

# Create Ordered dictionary
ordict = OrderedDict(sorted(freqdict.items(),
                            key=lambda item: item[1], reverse=True))

# Ignore top 10%
top10 = int(len(ordict.keys()) / 10)

# Print 100 words of the top 90%
print(list(ordict.items())[top10:top10 + 100])



