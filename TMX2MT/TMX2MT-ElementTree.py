#Convert TMX to MT Source and Target files using XML ElementTree
#Command: python3 TMX2MT-ElementTree.py <tmx_file_name> <source_lang> <target_lang>
#Note: <source_lang> <target_lang> must be the actual language codes used in the TMX file.


import xml
import xml.etree.ElementTree as ET
import sys

file = sys.argv[1]
source = sys.argv[2]
target = sys.argv[3]
source_file = file + "." + source
target_file = file + "." + target

tree = ET.parse(file)  
root = tree.getroot()

with open(source_file, "w+") as source_file, open(target_file, "w+") as target_file:
	for tu in root.iter('tu'):
	    for tuv in tu.iter('tuv'):
	        lang = list(tuv.attrib.values())
	        #print(lang[0])
	        if lang[0].lower() == source.lower():
	            for seg in tuv.iter('seg'):
	                source_text = seg.text
	                source_file.write(source_text + "\n")
	                #print(source_text)
	        elif lang[0].lower() == target.lower():
	            for seg in tuv.iter('seg'):
	                target_text = seg.text
	                target_file.write(target_text + "\n")
	                #print(target_text)

print("=> Done! Check the output files at:", source_file.name, target_file.name, sep="\n")
