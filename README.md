# moduli-iiserp
Notes and handouts for the moduli theory seminar at IISER Pune (ongoing from August 2020)


Inspired by the Stacks Project, I have decided to "tag up" the notes. This is a four symbol identifier placed in the left margin of the document (just like in the Stacks Project pdf files). So, every time I make changes in the notes, the commit message will indicate the Tag that has been modified. Since, the notes are being updated in an extremely non-linear fashion, Tags provide a mechanism to pin-point to the exact location in the document where updates were made. The changes are non-linear, because I am writing the notes "by topic", instead of "by lecture". You can look at the slide to get an idea of what was discussed on a particular day (Note: slides contents overlap, because material spills over into subsequent sessions).

The workflow for "tagging up" is as follows:

1. cd moduli-iiserp/Notes. We will run the scripts on this path.
2. Run tagger.py, python3 ../Scripts/tagger.py >> tags
3. Run add_tagger.py, python3 ../Scripts/add_tagger.py
4. Run compiler.py, python3 ../Scripts/compiler.py

Note: The cleanup.py can be used to remove tags from the tag_notes.tex file. Use Notes.tex to write the notes. 


The script 'tagger.py' is taken from the Gerby project at https://github.com/gerby-project 

The script 'add_tagger.py' is written by Aniket Gaur.

