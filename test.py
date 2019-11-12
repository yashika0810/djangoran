'''
x= int(input('please enter an integer'))
if x<0:
    if(x>-5):
        print('result is greater than -5')
    else:
        print("result is less than -5")
elif x==0:
    print('result is o')
elif x>0 and x<30:
    print('result is positive and within range 30')
else:
    print('result is greater than 30')



#using break and continue:

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


 #using else with loops
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))



#break and continue

while True:
    print ("Enter the number but -1 will quit the loop and -2 will keep you in a loop")
    x=int(raw_input("enter the choice:"))
    if x==-1:
        break
    if x==-2:
        continue
    print ("Hello I am inside the loop")
 
print ("I am outside of the loop")


avg=0.0
total=0
count=0
print ("Enter the grade(-1 to quit the program)")
grade=int(input("Enter the Grade"))
while grade!=-1:
    total=total+grade
    count=count+1
    print ("Enter the grade(-1 to quit the program)")
    grade=int(input("Enter the Grade"))
    if count==5:
        break
 
print("I am outside the loop")
avg=total/count
print ("Average of the subjects:",avg)

x = [0, 10, 20, 40, 100]
for i in x:
    print ('list element:',i)
print('The list has', len(x), 'elements')




x=[1,2,3,4,5]
for i in range(len(x)):
    x[i]=x[i]*2
print(x)

sum=0



avg=0
total=0
count=0
print("enter the grade(-1 to quit)")
grade=int(input("Enter the grade"))
while grade!=-1:
    total=total+grade
    count=count+1
    print("Enter grade")
    grade=int(input("Enter the grade"))
    if count==4:
        break

print("I am outside of the loop")
avg=total/count
print("avg is",avg)
 
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


# For-Else Syntax

for item in seq:
    statement 1
    statement 2
    if <cond>:
        break
else:
    statements

for i in range(3):
    for x in range(10,14):
        for y in range(100,105):
          print(i,x,y)

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)




for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


for i in range(3):
    for x in range(10,14):
        print(i,x)


for val in range(5):
	print(val)
else:
	print("The loop has completed execution")


for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")



def add():
    x=10
    y=20
    result=x+y
    return result
a=add()
print(a)




#The else block just after for/while is executed only when the loop is
# NOT terminated by a break statement.


x=[1,5,7]
for ele in x: 
    if ele % 2 == 0: 
        print ("list contains an even number") 
        break
  
    # This else executes only if break is NEVER 
    # reached and loop terminated after all iterations.   
else:    
    print ("list does not contain an even number") 
  

n=int(input("Enter the no"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i*i

print(d)

s = input("ENter the sentence")
d={"DIGITS":0, "LETTERS":0}
for i in s:
    if i.isdigit():
        d["DIGITS"]+=1
    elif i.isalpha():
        d["LETTERS"]+=1
    else:
        pass     #executes nothing
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])

word="letter" #word = "1"
count=1
length=""
for i in range(1,len(word)):
    if word[i-1]==word[i]:
        count+=1
    else :
        length += word[i-1]+" repeats "+str(count)+", "
        count=1
length += ("and "+word[i]+" repeats "+str(count))
print(length)

#with aruguement with return type
def add(a,b):
    print('this is the first type')
    return a+b
x=add(2,3)
print(x)


#without arguement with return type
def add():
    print('this is the second type')
    a=int(input("enter value of a "))
    b=int(input("enter value of b"))
    return a*b
x=add()
print(x)



#with arguement without return type

def add(a,b):
    print('this is the third type')
    print(a+b)
x=add(2,3)
print(x)


#without arguement without return type


def add():
    print('this is the fourth type')
    a = int(input("enter value of a "))
    b = int(input("enter value of b"))
    print(a+b)
x=add()
print(x)
print(type(x))


while True:
    try:
        x=int(input("enter no"))
        y=int(input("enter no"))
        avg=(x+y)/2
        print(avg)
    


try:
    f=open('data.txt','r')
    x=input("enter a value")
    f.write(x)

except:
    print("error")
finally:
    f.close()

from sys import argv
nameofprogram , filename=argv
 
print ("Name of the program is: ", nameofprogram)
print ("Name of the file is :",filename)
 

while True:
    try:
        fh=open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print("Provide correct name")
        try_again=input("Do you want to try again!! Press 'Y' for Yes and 'N' for no (Y/N):")
        if try_again=="Y":
            filename=input("enter the filename correctly this time")
        else:
            break
        


try:
    filehandler=open('dta.txt','r')
    content=filehandler.read()
    print(content[:20])
    print(type(content))
    filehandler.close()
    
except:
    print("enter the right name")




from collections import Counter
def test(word):
  a=list(word)
  coun=Counter(a)
  for i in a:
    print(i,coun[i])



test("letter yashika")


import csv
csvdata=[["NAME",'AGE'],['ABC','XYZ']]
with open('testing.csv','w') as csvfile:

    result=csv.writer(csvfile)
    result.writerows(csvdata)
  
def decorator(fun1):
    def inner():
        print("This is before function execution")
       # x=input("enter a value")
        #y=input("enter another value")
       # res=x+y
        #print (res)
        fun1()
    return inner
#@decorator
def needd():
    print ("hello i need to be decorated")
needd=decorator(needd)

needd()


class employee:
    def name(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
obj1=employee()
obj1.name("yashika","khatri")

class candidate:
    def check(self,par1,par2):
        return par1+par2
obj1=candidate()
obj1.check(1,2)
'''
class candidate:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def customfunc(self):
        print("dwj",self.name)
obj1=candidate("yashi","23")
print(obj1.customfunc())



