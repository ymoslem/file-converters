# file-converters
Converting bilingual translation files to the MT format: `file.source` and `file.target`

## TMX2MT

Converts a TMX translation memory into two files, source and target, for machine translation training.

There are two scripts that do the same thing, one with XML `minidom` and one with XML `ElementTree`. Please note that [TMX2MT-ElementTree.py](https://github.com/ymoslem/file-converters/tree/main/TMX2MT) is supposed to be faster, and supports segments that contain **inline tags**.

Whatever script you decide to use, run it in the Terminal/CMD as follows:
```
python3 <script.py> <tmx_file_name.tmx> <source_lang> <target_lang>
```

## Questions
If you have questions or suggestions, please feel free to [contact](https://blog.machinetranslation.io/contact/) me.

