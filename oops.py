class candidate:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def customfunc(self):
        print("Coming from customfunc and my name is",self.name)
obj1=candidate("yashika","24")
print(obj1.customfunc())



class consultadd:     #Parent/super/base
    def __init__(self,domain):
        self.domain=domain
    def getname(self):
        return self.domain
    def candidateattending(self):
        return False

class pcandidate(consultadd):
    def candidateattending(self):
        return True

c=consultadd("Python")
print(c.getname(),c.candidateattending())
p=pcandidate("Java")
print(p.getname(),p.candidateattending())




#Polymorphism:

class candidate:
    def domain(self):
        print("I am learning Python")
    def language(self):
        print("I am a Python student")
    def level(self):
        print("intermediate")

class Trainer:
    def domain(self):
        print("I am a trainer")
    def language(self):
        print("I train Python")
    def level(self):
        print("Expert in Python")

c=candidate()
t=Trainer()
c.domain()
for i in (c,t):
    i.domain()
    i.language()
    i.level()







