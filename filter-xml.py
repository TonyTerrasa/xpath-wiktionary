"""
Author: Tony Terrasa

A script which filters away the body text of the articles from 
an English Wiktionary data dump in XML format. 
"""
import sys 

# input file name, first argument
filename = sys.argv[1]
# the number of page entries you want to keep
num_entries = int(sys.argv[2]) 


f = open(filename, "r") # original file
output_file = open("output.xml", "w")

entry = 0
skipping = False

while entry < num_entries:

    line = f.readline()

    # check if we are skipping
    if skipping:
        # if skipping, see if we hit the end
        if "</text>" in line:
            skipping = False
            entry += 1
        # regarless, skip this line
        continue

    
    # if not skipping, see if we should be and change the state
    if "<text" in line:
        skipping = True
        continue

    # otherwise, write the line 
    output_file.write(line)

# finally, add the final required lines to make it valid xml
output_file.write("</revision>")
output_file.write("</page>")
output_file.write("</mediawiki>")

f.close()
output_file.close()

