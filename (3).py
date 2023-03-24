import re
text = input('Введите текст: ').lower()
text1 = input('Введите текст: ').lower()
text = re.sub("[$|@|&| |,|.|#|№|%|<|>|/|*|+|=|_|'|`|~|^|?|!|:|;|(|)|{|}]","",text) ## от знаков - \ | " ' [ ] избавиться не удалось
text1 = re.sub("[$|@|&| |,|.|#|№|%|<|>|/|*|+|=|_|'|`|~|^|?|!|:|;|(|)|{|}]","",text1)
text = sorted(text)
text1 = sorted(text1)

if text == text1:
    print('Yes')
else:
    print('No')