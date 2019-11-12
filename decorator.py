def decorator(func1):
    def random():
        print("This is before program execution")
        x=int(input("enter a value"))
        y=int(input("enter second value"))
        res=x+y
        print(res)
        func1()
    return random
#Main code starts

@decorator
def need():
   print("Hello I need to be decorated") 
#need=decorator(need)
need()


