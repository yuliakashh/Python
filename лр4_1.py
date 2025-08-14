class Person():
    citizenship='Гражданство России'
    city='Москва'
    def __str__(self):
        return 'метод __str__ Класс Person'+'\n'+self.citizenship+ '\n' + self.name +'\n'+ self.date+'\n'+self.passport
    def set_av_inc(self,i):
        self.av_inc=i
    def get_av_inc(self):
        print('Средний доход = ',self.av_inc)
    def __init__(self,p='3012998765',d='23.09.2000',n='Иван'):
        print('Работает конструктор базового класса')
        self.name = n
        self.date = d
        self.passport = p
    def func_1(self):
        print ('работает переопределяемый метод (баз.кл.) ->', self.city)
class School(Person):
    def __init__(self,s):
        print('работает конструктор School')
        self.school=s
        super().__init__()
    def __str__(self):
        return 'метод __str__ Класс School'+'\n'+self.school
class Student (Person):
    group='ИБМ6-23Б'
    def __init__(self,v,s):
        print('работает конструктор Student')
        self.vuz = v
        self.spec = s
        super().__init__()
    def func_1(self):
        print('работает переопределенный метод, ', self.group)
    def __str__(self):
        return 'метод __str__  Класс Student'+'\n'+self.vuz+'\n'+self.spec
print("""Меню. Выбор типа объекта демонстрации.
1. Человек. 
2. Школьник. 
3. Студент. 
4. Выход.""")
while True:
    v=int(input('Ваш выбор(без точки) -->> '))
    if v==1:
        print ('Человек')
        a=Person()
        a.func_1()
        a.set_av_inc(0)
        a.get_av_inc()
        print(a)
    if v==2:
        print('Школьник')
        b=School('МБОУ № 23')
        a.set_av_inc(3000)
        a.get_av_inc()
        print(b)
    if v==3:
        print ('Cтудент')
        c=Student('МГТУ','Бизнес-информатика')
        c.func_1()
        a.set_av_inc(5000)
        a.get_av_inc()
        print(c)
    if v==4:
        exit()