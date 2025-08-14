f=open('file1', 'r')
sum=0
while True:
    s=f.readline()
    if not s:
        break
    l=s.split()
    for i in range (len(l)):
        try:
            sum = sum + int(l[i])
        except ValueError:
            print('Встретилось не число!')
            exit()
f.close()
print(sum)
f3=open('f3.txt','w')
f3.write(str(sum))
f3.close()