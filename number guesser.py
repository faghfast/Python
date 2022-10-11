import random
def start(number):
    x = random.randint(0, number)
    print('Загадал. Попробуй отгадать)')

    while True:
        n = input()

        if n.isdigit():
            if x == int(n):
                print('Прямо в яблочко)')
                break
            elif x > int(n):
                print('Неа, больше)')
            else:
                print('Неа, меньше)')
        else:
            print('Я так не играю. Напиши целое число в диапазоне от 0 до', number)



print('Привет. Давай сыграем в угадайку?')
print('Ты мне назовешь целое число n от 1 до 100, я загадаю число от 0 до n, а ты его попробуешь угадать?')
print('Есть желание - напиши "да"')

while True:
    go = input().lower()
    if go == 'да':
        print('Отлично, напиши целое число от 1 до 100')
        break
    else:
        print(':(')

while True:
    num = input()
    if num.isdigit() and 1 <= int(num) <= 100:
        start(int(num))
        break
    else:
        print('Мне нужно целое число от 1 до 100. Я по-другому не умею (')

