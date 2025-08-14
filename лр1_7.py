s=str(input('Введите действительные числа через пробел: '))
l=s.split()
sum=0
for i in range (len(l)):
    try:
        sum=sum+float(l[i])
    except ValueError:
        print(l[i],' - это не число')
print(sum)