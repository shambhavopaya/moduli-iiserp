import glob
import re
import subprocess
import shutil



# no I, no O
CHARACTERS = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"

# convert integer to tag
tags = dict()
labels = dict()
inactive = []

try:
  with open("tags") as f:
    for line in f:
      # actual tag
      if not line.strip().startswith("#"):
        key,value = line.strip().split(",")
        tags[key] = value
        labels[value] = key

      # check for inactive tags too
      elif len(line.split(",")) == 2 and len(line.split(",")[0]) == 4:
        inactive.append(line.split(",")[0])

except FileNotFoundError:
  pass


filenames = ["tag_notes.tex"]


for filename in filenames:
  file_data = open(filename).read()
  for key in tags.keys():
      if "\label{"+ tags[key] + "}\marginnote{" + key + "}" in file_data :
          file_data = file_data.replace("\marginnote{" + key + "}", '')
  #new_filename = filename.replace("tag_notes.tex","cleanup_notes.tex")
  file = open(filename,"w")
  file.write(file_data)
  file.close()


