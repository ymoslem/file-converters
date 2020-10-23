#Convert TMX to MT Source and Target files using XML minidom
#Command: python3 TMX2MT-minidom.py <tmx_file_name> <source_lang> <target_lang>
#Note: <source_lang> <target_lang> must be the actual language codes used in the TMX file.


from xml.dom import minidom
import sys


file = sys.argv[1]
source = sys.argv[2]
target = sys.argv[3]
source_file = file + "." + source
target_file = file + "." + target

mytmx = minidom.parse(file)

segments = mytmx.getElementsByTagName('tu')

# number of segments
print("=>", len(segments), "segments are in the file.")


with open(source_file, "w+") as source_file, open(target_file, "w+") as target_file:
    for segment in segments:
        tuvs = segment.getElementsByTagName('tuv')
        for tuv in tuvs:
            lang = tuv.attributes['xml:lang'].value
            if  lang.lower() == source.lower():
                source_text = tuv.getElementsByTagName('seg')
                source_text = source_text[0].firstChild.data
                #print(lang, source)
                source_file.write(source_text + "\n")
            elif lang.lower() == target.lower():
                target_text = tuv.getElementsByTagName('seg')
                target_text = target_text[0].firstChild.data
                #print(lang, target, '\n')
                target_file.write(target_text + "\n")

print("=> Done! Check the output files at:", source_file.name, target_file.name, sep="\n")

