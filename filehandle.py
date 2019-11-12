'''
with open('data.txt','r') as file:

    data=file.readline()
    for i in data:
        word=i.split()
     print(word)
     
try:
    fh=open('data.txt','r')
    content=fh.read()
    print(content[:20])
    print(type(content))
    fh.close()
except:
    print("enter the right name of the file")



from sys import argv
nameofprogram, filename=argv

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
        print("The name entered is wrong! Provide a correct name")
        try_again = input("Do you want to try again!! Press the button 'Y' if yes and press 'N' if no (Y/N):")
        if try_again=="Y":
         filename = input("Please provide the name correctly this time")
        else:
         break


import csv
with open('testing.csv','r') as csvfile:
    result=csv.reader(csvfile)
    for i in result:
        print(i)
        
'''


import csv
csv_data=[['NAME','AGE'],['ABC','35'],['XYZ','34']]

with open('person.csv','w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(csv_data)


