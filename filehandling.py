'''with open("data.txt",'r') as file:
    data=file.readline()
    for i in data:
        word=i.split()
        print(word)


try:
    fh=open("dat.txt",'r')
    content=fh.read()
    print(content[:20])
    fh.close()
except:
    print("Enter the correct name of the file")

    


from sys import argv
nameofprogram , filename=argv

print("Name of program",nameofprogram)
print("Name of file",filename)

while True:
    try:
        fh=open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print("The name entered is wrong. Please provide correct name")
        try_again=input("Do you want to try again? If yes then press the button 'Y' and if no then press 'N' (Y/N:)")
        if try_again=='Y':
            filename = input("Please provide the correct name of file this time")
        else:
            break





'''

import csv
with open('test.csv','r') as csvfile:
    result=csv.reader(csvfile)
    for i in result:
        print(i)