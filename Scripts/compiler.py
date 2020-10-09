import subprocess
import shutil



#file = input('')

subprocess.check_call(['pdflatex', 'tag_notes.tex'])
subprocess.check_call(['bibtex', 'tag_notes'])
subprocess.check_call(['pdflatex', 'tag_notes.tex'])
subprocess.check_call(['pdflatex', 'tag_notes.tex'])

shutil.move("tag_notes.pdf", "Notes.pdf")
