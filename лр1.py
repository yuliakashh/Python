def function(n,s,a,b):
    f = open(n, 'w')
    import random
    for i in range(s):
        for k in range(4):
            f.write(str(round(random.uniform(a, b), 2)) + '  ')
        f.write('\n')
    f.close()
name=str(input('Введите название файла: '))
try:
    stroki=int(input('Введите количество строк: '))
except ValueError:
    while True:
        print('Введено не число')
        print('Повторить ввод? да/нет')
        q = str(input())
        if (q == 'да') or (q == 'Да'):
            stroki = input('Введите количество строк: ')
            if stroki.isdigit():
                stroki=int(stroki)
                break
        else:
            exit()
try:
    a=int(input('Введите левую границу диапазона чисел: '))
except ValueError:
   while True:
        print('Введено не число')
        print('Повторить ввод? да/нет')
        q = str(input())
        if (q == 'да') or (q == 'Да'):
            a=input('Введите левую границу диапазона чисел: ')
            if a.isdigit():
                a=int(a)
                break
        else:
            exit()
try:
    b=int(input('Введите правую границу диапазона чисел: '))
except ValueError:
    while True:
        print('Введено не число')
        print('Повторить ввод? да/нет')
        q = str(input())
        if (q == 'да') or (q == 'Да'):
            b=input('Введите правую границу диапазона чисел: ')
            if b.isdigit():
                b=int(b)
                break
        else:
            exit()
function(name, stroki, a, b)
try:
    f=open(name, 'r')
    print(*f)
    f.close()
    f=open(name, 'r')
except FileNotFoundError:
    print('Файл не найден')
f2=open('file2.txt', 'w')
readline_number=-1
p=[]
z=0
while True:
    a=f.readline()
    b=a
    readline_number = readline_number + 1
    if not a:
        break
    a=a.split()
    if len(a)!=4:
        print ('В строке № ' + str(readline_number)+' не хватает координат(ы) ')
        print(b)
        z=1
if z==1:
    exit()
f.close()
f=open(name, 'r')
readline_number=-1
while True:
    a=f.readline()
    if not a:
        break
    p.append(0)
    readline_number=readline_number+1
    z=0
    v=0
    y=0
    for i in range(0,len(a)):
        if ((a[i].isdigit()) or (a[i]=='.')) and (y==1):
            y=2
            continue
        if ((a[i].isdigit()) or (a[i] == '.')) and (v==1):
            break
        if (a[i].isdigit()) or (a[i]=='.'):
            continue
        elif (a[i]==' '):
            if y==2:
                z=p[readline_number]
                p[readline_number]=z +1
                v=1
            elif y==0:
                y=1
s=0
for i in range (len(p)):
    s=s+p[i]
    f2.write(str(p[i]))
    f2.write('\n')
print(p)
print('Среднее расстояние = ',s/len(p))


