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

langs = []

for segment in segments:
    tuvs = segment.getElementsByTagName('tuv')
    for tuv in tuvs:
        lang = tuv.attributes['xml:lang'].value
        langs.append(lang.lower())

langs = set(langs)

if source in langs and target in langs:
            
    with open(source_file, "w+", encoding='utf-8') as source_file, open(target_file, "w+", encoding='utf-8') as target_file:
        for segment in segments:
            tuvs = segment.getElementsByTagName('tuv')
            for tuv in tuvs:
                lang = tuv.attributes['xml:lang'].value
                if  lang.lower() == source.lower():
                    source_text = tuv.getElementsByTagName('seg')
                    try:
                        source_text = source_text[0].firstChild.data
                        #print(lang, source)
                    except:
                        continue
                    source_file.write(source_text + "\n")
                elif lang.lower() == target.lower():
                    target_text = tuv.getElementsByTagName('seg')
                    try:
                        target_text = target_text[0].firstChild.data
                        #print(lang, target, '\n')
                    except:
                        continue
                    target_file.write(target_text + "\n")

    print("=> Done! Check the output files at:", source_file.name, target_file.name, sep="\n")

else:
    print("Please correct the language codes. Found language codes are:", *langs)    
