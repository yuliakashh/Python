def __str__ (self):
    return f"{self.name}"
class Disciplina:
    """Описание дисциплины"""
    method =__str__
    def set_hours (self,q):
        self.hours=q
    def set_name (self,q):
        self.name=q
    def set_sem (self,q):
        self.sem=q
    def __init__(self,n,s,h):
        self.set_name(n)
        self.get_name()
        self.set_hours(h)
        self.get_hours()
        self.set_sem(s)
        self.get_sem()
    def get_hours(self):
        print('get(self) значение поля self.hours = ',self.hours)
    def get_sem(self):
        print ('get(self) значение поля self.sem = ',self.sem)
    def get_name(self):
        print ('get(self) значение поля self.name = ',self.name)
    def __del__(self):
        print('проверка работы деструктора')
a=Disciplina('программирование',8,99)
print(a.method())
