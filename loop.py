'''
avg=0
total=0
count=0
print("Enter the grade(-1 to quit)")
grade=int(input("Please enter the grade"))
while grade!=-1:
    total=total+grade
    count=count+1
    print("Enter the grade(-1 to quit)")
    grade=int(input("Please enter the grade"))
    if count==4:
        break


print("I am outside the loop")
avg=total/count
print("Average of subjects",avg)
    


x=[1,2,4,5,6]
for i in x:
    print("list elements:",i)
print("The list has", len(x),'elements')


x=[1,2,4,5,6,7,4,6]
print("List before multiplication",x)
#this is my data sequence


#range(len(x))---> len(x)-->8 range(8)--> 1,2,3,4,5,6,7
for i in range(len(x)):
    x[i]=x[i]+5
print(print("List after multiplication",x))

#1+2+3+4+5....
sum=0
for val in range(1,21): 
    sum=sum+val
print(sum)




for i in range(3):
    for x in range(10,14):
        for y in range(100,104):
         print(i,x,y)



for val in range(5):
    print(val)
else:
 print("The loop has completed execution")

 
for x in range(10):
     if x % 2==0:
         continue
     print(x)



for x in [1]:
    print("Then")
print("Else")



for i in range(1,10):
    if(i%11==0):
        break
    print(i)
else:
    print("it will execute only when loop is not terminated by break")


#The else block is executed only when the loop is NOT TERMINATED BY A BREAK

x=[1,2,3]
for elements in x:
    if elements % 2==0:
        print("My list contains an even no")
        break
    
else:
    print("My list does not contain even no")



x=int(input("Enter a no"))
d=dict()
for i in range(1,x+1):
    d[i]=i*i*i
print(d)

'''
#Consultadd1234
#LETTERS-10 DIGITS-4

s=input("Enter any sentence")
d={"DIGITS":0,"LETTERS":0}
for i in s:
    if i.isdigit():
        d["DIGITS"]+=1
    elif i.isalpha():
        d["LETTERS"]+=1
    else:
        pass    #executes nothing
print('LETTERS:',d['LETTERS'])
print('DIGITS:',d['DIGITS'])

    





