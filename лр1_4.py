s=0
while True:
    try:
        a=float(input('Введите целое число --> '))
    except ValueError:
        print('Введено не число')
    else:
        s=s+a
    o=str(input('Продолжить ввод? да/нет '))
    if (o!='да') and (o!='Да'):
        break
print('Сумма введенных чисел = ',s)