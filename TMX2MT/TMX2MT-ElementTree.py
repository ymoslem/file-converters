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

langs = []

for tu in root.iter('tu'):
    for tuv in tu.iter('tuv'):
        lang = list(tuv.attrib.values())
        langs.append(lang[0].lower())

langs = set(langs)

if source in langs and target in langs:
    with open(source_file, "w+", encoding='utf-8') as source_file, open(target_file, "w+", encoding='utf-8') as target_file:
        for tu in root.iter('tu'):
            for tuv in tu.iter('tuv'):
                lang = list(tuv.attrib.values())
                #print(lang[0])
                if lang[0].lower() == source.lower():
                    for seg in tuv.iter('seg'):
                        source_text = ET.tostring(seg, 'utf-8', method="xml")
                        source_text = source_text.decode("utf-8")
                        source_text = re.sub('<.*?>|&lt;.*?&gt;|&quot;|&apos;|{}', ' ', source_text)
                        source_text = re.sub(r'[ ]{2,}', ' ', source_text).strip()
                        source_file.write(str(source_text) + "\n")
                        #print(source_text)
                elif lang[0].lower() == target.lower():
                    for seg in tuv.iter('seg'):
                        target_text = ET.tostring(seg, 'utf-8', method="xml")
                        target_text = target_text.decode("utf-8")
                        target_text = re.sub('<.*?>|&lt;.*?&gt;|&quot;|&apos;|{}', ' ', target_text)
                        target_text = re.sub(r'[ ]{2,}', ' ', target_text).strip()
                        target_file.write(str(target_text) + "\n")
                        #print(target_text)

    print("=> Done! Check the output files at:", source_file.name, target_file.name, sep="\n")

else:
    print("Please correct the language codes. Found language codes are:", *langs)
