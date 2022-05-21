"""

This Program deletes all the files that do not have any occurences of the
word that you are looking for, which greatly reduces the space taken up on
the drive and also makes everything more readable for the user.

"""

import os

# Path where text files are located
path = "D:/transcript_python_project"
# List of words that are in supposed to be in the files
words = ['firework']

files = os.listdir(path)
for each_file in files:
    full_path = "%s/%s" % (path, each_file)
    # This code reads the content of each file.
    # The "encoding="ISO-8859-1"" part is to make sure that the code doesn't break for some reason.
    each_file_content = open(full_path, 'r', encoding="ISO-8859-1").read()
    # If the files don't contain any of the words in the word list, and
    # if the file is a .txt file, 
    # then delete those files.
    if not any(word in each_file_content for word in words) and each_file.endswith(".txt"):
       os.unlink(full_path)
