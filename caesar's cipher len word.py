encrypt = input()


def cipher(sentence):
    a = [list(i) for i in sentence.split()]
    for i in a:
        key = 0
        for c in i:
            if c.isalpha():
                key += 1
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


cipher(encrypt)
