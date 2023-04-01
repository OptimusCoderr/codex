"""""
s="PUTHON"
k=" Its good for data science"
price=18
print(type(s))
print(s + k)
print(s + k +" " +str(price))

#INDEXING AND SCLICING
a= "GAME OF PRORAMMING"
print(a[3:8])
print(a[-8:-3])
print(a[-1])
print (a[0:12:2])# s[start:end:stepsize]
print(a[::-1])#reverse

#EDITING STRINGS
a= "    A lot Of spaces at the    Beginning and end    "
b= a.strip()
print(b.lower())
print(b.upper())
print(a.replace("A","B"))

L=print(a.split("at"))
print("lot" in a)
print("lot"=="lot")
print("abaooob"<"zkk")#alpahbetic order
print("djsnhkrjh\"string\"here")
print('We are "Learning"')
print("We are\nin a new line")
print("We are\tin a new line")
print(r"c:\name\drive")

"""""

def getdatafrom():
    D={}
    while True:
        studentId=input("Enter student id:")
        marklis=input("Enter the marks by comma separated values")
        morestudents=input("Enter 'no'for to stop adding students\n")
        if studentId in D:
            print(studentId, " is already inserted")
        else:
            D[studentId]= marklis.split(",")
        if morestudents.lower()=="no":
            return D

std=getdatafrom()
print(std)

def getavgmarks(D):
    avgD={}
    for x in D:
        L=D[x]
        s=0
        for marks in L:
            s+=int(marks)
        avgD[x]=s/len(L)
    return avgD

avgm=getavgmarks(std)
for x in avgm:
    print("student:",x,"got average marks as:", avgm[x])
