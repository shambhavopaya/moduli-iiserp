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



filenames = ["notes.tex"]


for filename in filenames:
  file_data = open(filename).read()
  for key in tags.keys():
      if "\label{"+ tags[key] + "}\marginnote{" + key + "}" not in file_data :
          file_data = file_data.replace("\label{"+ tags[key] + "}" ,"\label{"+ tags[key] + "}\marginnote{" + key + "}")
  new_filename = filename.replace("notes.tex","tags_notes.tex")
  file = open(new_filename,"w")
  file.write(file_data)
  file.close()

subprocess.check_call(['pdflatex', 'cleanup_notes.tex'])
subprocess.check_call(['bibtex', 'cleanup_notes'])
subprocess.check_call(['pdflatex', 'cleanup_notes.tex'])
subprocess.check_call(['pdflatex', 'cleanup_notes.tex'])
