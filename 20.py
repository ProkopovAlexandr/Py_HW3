def fun(smb):
    for key in dct:
        if smb in key:
            return dct.get(key)

lng = input('Выбирите язык ("en" или "ru"): ')

if lng == "en":
    dct = {
        'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3,
        'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}
elif lng == "ru":
    dct = {
        'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3,
        'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}

print(sum(map(fun, input('Введите слово: ').upper())))