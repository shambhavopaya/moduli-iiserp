import glob
import re

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



filenames = ["Moduli Theory Seminar Notes.tex"]


for filename in filenames:
  file_data = open(filename).read()
  for key in tags.keys():
      if "\label{"+ tags[key] + "}\marginnote{" + key + "}" not in file_data :
          file_data = file_data.replace("\label{"+ tags[key] + "}" ,"\label{"+ tags[key] + "}\marginnote{" + key + "}")
  new_filename = filename.replace(".tex","1.tex")
  file = open(new_filename,"w")
  file.write(file_data)
