import subprocess
import shutil



file = input('')

subprocess.check_call(['pdflatex', file +'.tex'])
subprocess.check_call(['bibtex', file])
subprocess.check_call(['pdflatex', file + '.tex'])
subprocess.check_call(['pdflatex', file + '.tex'])

shutil.move(file +'.pdf', "notes.pdf")
