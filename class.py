#Abstraction  
from abc import abstractmethod
class emp:
  @abstractmethod
  def daysal(self,hr,r):
    pass
  @abstractmethod
  def Monthsalary(self):
    pass
  @abstractmethod
  def Text(self,x):
    pass
  @abstractmethod
  def Absent(self,a):
    pass
  @abstractmethod
  def Totalsal(salf):
    pass

class Engineer(emp):
  def daysal(self,hr,r):
    global day
    day=hr*r
    print(day)
  def Monthsalary(self):
    global month
    month=day*30
    print(month)
  def Text(self,x):
    global text
    text=month*x/100
    print(text)
  def Absent(self,a):
    global ab
    ab=day*a
    print(ab)
  def Totalsal(self):
    total=month-text-ab
    print(total)


k=Engineer()
k.daysal(5,600)
k.Monthsalary()
k.Text(6)
k.Absent(5)
k.Totalsal()