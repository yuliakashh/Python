def __str__ (self): #метод, описанный мне класса
    return self.name+','+str(self.sem)+ ' '+ str(self.hours)
class Disciplina:
    """Описание дисциплины"""
    def __str__(self):  # метод, описанный мне класса
        return self.name + ',' + str(self.sem) + ' ' + str(self.hours)
    def set_hours (self,q):
        self.hours=q
    def set_name (self,q):
        self.name=q
    def set_sem (self,q):
        self.sem=q
    def __init__(self,n,s,h):
        self.set_name(n)
        #self.get_name()
        self.set_hours(h)
        #self.get_hours()
        self.set_sem(s)
        #self.get_sem()
    def get_hours(self):
        print('get(self) значение поля self.hours = ',self.hours)
    def get_sem(self):
        print ('get(self) значение поля self.sem = ',self.sem)
    def get_name(self):
        print ('get(self) значение поля self.name = ',self.name)
    def __del__(self):
        print('проверка работы деструктора')
print("""Меню
1. Вывод строки документации класса. 
2. Создание экземпляров класса. 
3. Создание списка экземпляров класса. 
4. Вывод списка на экран.
5. Сортировка списка. 
6. Поиск максимального элемента списка. 
7. Поиск минимального элемента списка.
8. Выход.""")
while True:
    v=int(input('Ваш выбор(без точки) -->> '))
    if v==1:
        print(Disciplina.__doc__)
    elif v==2:
        k = int(input('Введите N - количество экземпляров разработанного класса --> '))
        imena = []
        for u in range (k):
            e='a'+str(u)
            imena.append(e)
        import random
        dis = ['Дифференциальные и разностные уравнения', 'Иностранный язык', 'Электронный бизнес', 'Микроэкономика',
           'Программирование']
        for i in range(k):
            s=random.randint(0,11)
            n=random.choice(dis)
            h=random.randint(71,181)
            imena[i-1]=Disciplina(n,s,h)
            print ('Экземпляр ',imena[i-1])
    elif v==3:
        m = int(input('Введите M - количество экземпляров класса --> '))
        import random
        dis=['Дифференциальные и разностные уравнения','Иностранный язык','Электронный бизнес','Микроэкономика','Программирование']
        list=[]
        imena=[]
        for u in range (m):
            e='a'+str(u)
            imena.append(e)
        for i in range (m):
            n = random.choice(dis)
            s=random.randint(0,11)
            h = random.randint(71, 181)
            imena[i-1]=Disciplina(n,s,h)
            list.append(imena[i-1])
        print('Создан список эеземпляров класса')
    elif v==4:
        for i in range(len(list)):
            print('Экземпляр ',list[i])
        #print('выводится список экземпляров', list)
    elif v==5:
        list = sorted(list, key=lambda x: x.hours)
        for i in range(len(list)):
            print('Экземпляр ',list[i])
    elif v==6:
        max_atr = max(list, key=lambda x: x.hours)
        print('экземпляр с максимальным атрибудом = ', max_atr)
    elif v==7:
        min_atr = min(list, key=lambda x: x.hours)
        print('экземпляр с минимальным атрибудом = ', min_atr)
    elif v==8:
        del list
        exit()

