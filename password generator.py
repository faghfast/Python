import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous_characters = 'il1Lo0O'
chars = ''

question1 = 'Включать ли цифры 0123456789? y/n'
question2 = 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n'
question3 = 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? y/n'
question4 = 'Включать ли символы !#$%&*+-=?@^_? y/n'
question5 = 'Исключить ли неоднозначные символы il1Lo0O? y/n'

def lenght_and_amount():
    while True:
        x = input()
        if x.isdigit() and int(x) > 0:
            return int(x)
        else:
            print('Введи целое число > 0')
            continue


def questions(question, string):
    x = ''
    global chars
    while x != 'y' and x != 'n':
        print(question)
        x = input()
    if x == 'y':
        chars += string
    else:
        print('ok')


def generate(amount, lenght):
    for _ in range(amount):
        print(*random.sample(chars, lenght), sep='')


print('Сколько паролей?')
amount = lenght_and_amount()

print('Длина?')
leng = lenght_and_amount()

questions(question1, digits)
questions(question2, lowercase_letters)
questions(question3, uppercase_letters)
questions(question4, punctuation)

f = ''
while f != 'y' and f != 'n':
    print(question5)
    f = input()

if f == 'y':
    chars = [i for i in chars if i not in ambiguous_characters]
else:
    print('ok')

generate(amount, leng)
