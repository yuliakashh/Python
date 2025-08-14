s=str(input('Введите целые числа через пробел: '))
l=s.split()
sum=0
for i in range (len(l)):
    try:
        sum=sum+int(l[i])
    except ValueError:
        continue
print(sum)