from random import choice
while True:
    print('Загадано четырехбуквенное слово из букв А,E,Н,О,С,Т.\nОтгадай!')

    s = ''

    while True:
        if len(s) == 4:
            break
        a = choice('АЕНОСТ')
        if not a in s:
            s += a

    for i in range(10):
        k = 0
        x = 0
        a = input('Попытка № %i:'%(i+1))
        if a == s:
            print('Вы выиграли!!!')
            break

        for wi, w in enumerate(s):
            v = a[wi]
            if w == v:
                k += 1
            elif v in s:
                x += 1
        print('На "своем месте": ', k)
        print('На "чужом месте": ', x)
        if i == 9:
            print('Вы проиграли')

    if input('Хотите начать новую игру?(да/нет):').strip().lower() != 'да':
        break
