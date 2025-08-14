try:
        f = open('задача3', 'r')
except FileNotFoundError:
        print('Такой файл не существует')
        exit()
s=0
while True:
        a=f.readline()
        if not a:
                break
        try:
                a=float(a)
        except ValueError:
                continue
        else:
                s=s+a
print('s=',s)

