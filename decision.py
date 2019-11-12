'''
x=int(input("Please enter a value"))
if x<0:
    if (x>-5):
        print("result is greater than -5")
    else:
        print("result is less than -5")
elif x==0:
    print("result is 0")
elif x>0 and x<30:
    print("result is postive and within the range 30")
else:
    print("result is greater than 30")

'''

while True:
    print("Enter any number but -1 will quit the loop and -2 will keep you in the loop")
    x=int(input("Give your choice"))
    if x==-1:
        break
    if x==-2:
        continue
        print("I am inside the loop")
print("I am outside the loop")


