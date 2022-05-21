"""

This program counts a certain word or words across all the files in the folder.

"""

# This code is not mine and can be found by following the below link
# https://stackoverflow.com/questions/17399535/to-count-the-word-frequency-in-multiple-documents-python

from glob import glob
from collections import Counter
import re
import os

folderpaths = 'D:/transcript_python_project'
counter = Counter()

filepaths = glob(os.path.join(folderpaths,'*.txt'))
for file in filepaths:
    with open(file, "r+") as f:
        #words = re.findall(r'\w+', f.read().lower())
        words = re.findall('firework', f.read().lower())
        counter = counter + Counter(words)
print(counter)
