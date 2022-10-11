effect = ''
language = ''
key = 'a'


def cipher():
    if language == 'ру':
        print('Пиши кирилицей')
        a = [list(i) for i in input().split()]
        for i in a:
            for j in range(len(i)):
                if 1071 >= ord(i[j]) >= 1040:
                    x = ord(i[j]) + int(key)
                    if x > 1071:
                        x -= 32
                    i[j] = chr(x)
                elif 1103 >= ord(i[j]) >= 1072:
                    x = ord(i[j]) + int(key)
                    if x > 1103:
                        x -= 32
                    i[j] = chr(x)
    else:
        print('Пиши латиницей')
        a = [list(i) for i in input().split()]
        for i in a:
            for j in range(len(i)):
                if 122 >= ord(i[j]) >= 97:
                    x = ord(i[j]) + int(key)
                    if x > 122:
                        x -= 26
                    i[j] = chr(x)
                elif 90 >= ord(i[j]) >= 65:
                    x = ord(i[j]) + int(key)
                    if x > 90:
                        x -= 26
                    i[j] = chr(x)
    print(*[''.join(i) for i in a])


def decipher():
    if language == 'ру':
        print('Пиши кирилицей')
        a = [list(i) for i in input().split()]
        for i in a:
            for j in range(len(i)):
                if 1071 >= ord(i[j]) >= 1040:
                    x = ord(i[j]) - int(key)
                    if x < 1040:
                        x += 32
                    i[j] = chr(x)
                elif 1103 >= ord(i[j]) >= 1072:
                    x = ord(i[j]) - int(key)
                    if x < 1072:
                        x += 32
                    i[j] = chr(x)
    else:
        print('Пиши латиницей')
        a = [list(i) for i in input().split()]
        for i in a:
            for j in range(len(i)):
                if 122 >= ord(i[j]) >= 97:
                    x = ord(i[j]) - int(key)
                    if x < 97:
                        x += 26
                    i[j] = chr(x)
                elif 90 >= ord(i[j]) >= 65:
                    x = ord(i[j]) - int(key)
                    if x < 65:
                        x += 26
                    i[j] = chr(x)
    print(*[''.join(i) for i in a])


while effect != 'д' and effect != 'ш':
    print('Ку! Шифруем или дешифруем? ш/д')
    effect = input()

while language != 'ру' and language != 'анг':
    print('Русский или английский? ру/анг')
    language = input()

while not key.isdigit():
    print('Какой шаг? (Целое число)')
    key = input()

if effect == 'ш':
    cipher()
else:
    decipher()
