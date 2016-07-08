f = open("TimeSheet.txt","r")
timeLines = f.readlines()

for time in timeLines:
    tList = time.split()
    #print(tList)
    if len(tList)>7:
        print(tList[0],"-",len(tList)-1,"practice sessions")
f.close()



f=open('TimeSheet.txt')
minNum=0
for line in f:
    thisList= line.split()
    minNum=thisList[1]
    for i in range(2, len(thisList)):
        if minNum>thisList[i]:
             minNum=thisList[i]
    print(thisList[0],' ', minNum)
         
f.close()



f1=open('TimeSheet.txt')
f2=open('Average.txt', 'w')
sum1=0
avg=0
for line in f1:
    thisList=line.split()
    for a in range(1, len(thisList)):
        sum1=sum1+int(thisList[a])
    avg=sum1/len(thisList)
    f2.write(thisList[0]+' '+str(avg)+'\n')
f1.close()
f2.close()




f=open('Average.txt', 'r')
print(f.readlines())
f.close()

f=open('Average.txt')
str1=f.readline()
line1=str1.split()
minNum1=line1[1]
for line in f:
    thisList=line.split()
    #print (thisList)
    minNum=thisList[1]
    if float(minNum1)>float(minNum):
        minNum1=minNum

print(minNum1)
f.close()


##     
