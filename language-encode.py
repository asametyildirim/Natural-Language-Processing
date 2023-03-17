#see the language encoding of the file

import chardet

with open('verim.txt', 'rb') as f:
    result = chardet.detect(f.read())
print(result['encoding'])
