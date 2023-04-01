
##IF CONDITION
a=int(input("Enter an integer:"))
b=int(input("Enter another integer:"))
if a>b:
    print("A is the larger number")
if a<b:
    print("B is the greatest number")
if a==b:
    print("They are the same")
else:
    print("STOP")

# another way to use it
if a>b:
    print("A is the larger number")
if a<b:
    print("B is the greatest number")
else:
    print("They are the same")
#ELSE IF
if a>b:
    print("A is the larger number")
elif a<b:
    print("B is the greatest number")
else:
    print("They are the same")

#   CODE
a= int(input("Enter Marks :"))
if a >= 85:
    print(" A GRADE")
elif (85<a) and (a>=80) :
    print ("A- GRAdE")
elif (a<80) and (a>=75):
    print("B GRADE")
elif (a<75) and (a>=70):
    print(" B- GRADE")
else:
    print("BELOW AVERAGE")

a=int(input("ENTER A NUMBER: "))
if a >10:
    print("No is larger than 10")
    if a>20:
        print(" No is also larger than 20")
    else:
        print("no is <= 20")
else:
    print("End of program")

"""
User will enter a floating point number let say 238.915. Your task is to find out the integer portion beifre the point
(in this case 238) an dthen check if that integer portion is an even number or not?

"""
x= float(input("Enter a real number: "))

if x>0 or x<0:
    y=int(x)
    print(y)
    # for positive and negative
    if y%2>0:
        print("ODD NO")
    else:
        print ("EVEN")
else:
    print("0")

#CONTROL FLOW (LOOPS)
n= int(input("Max iterations: "))
i=1
while (i<n):
    print(i)
    i+=1
print("done")

#printing even numbers
n=int(input("no of iterations:"))
i=1
while (i<=0):
    if (i%2==0):
        print(i)
    else:
        pass
    i+=1
print("DONE")

#BREAK AND CONTINUE
n=int(input("no of iterations:"))
i=1
while True:
    if (i%9==0):
        print("if")
        break
    else:
        print("else")
        i+=1
print("DONE")

#FOR LOOP
L=[]
for i in range(0,10,2):
    print(i)
    L.append(i**2)
    #print(L)
print(L)

s={'applw',4.9,'cherry'}
i=1
for x in s:
    print(x)
    i+=1
    if i==3:
        break
    else:
        pass
else:
    print('Loop cpletes iteration')
print("Outside the loop")

#EXPLORING A DICTIONARY IN FOR LOOP
D={"apple":44,"cherry": "game"}
for x in D:
    print(x,D[x])

#EXPLORING A DICTIONARY IN FOR LOOP
D={"A":44,"C": "game","B":"100"}
for x in D:
    print(x,D[x])

#EXERCISE for FOR loop
A=[1,2,4,-5,7,9,3,2]
for x in A:
    A[x].sort
    print(A[x])



#EXERCISE for FOR loop SORTING
A=[1,2,4,-5,7,9,3,2]

for j in range(len(A)):
    m=A[j]
    idx=j
    c=j
    for i in range(j,len(A)):
        if A[i]<m:
            m=A[i]
            idx=c
        c+=1
    temp= A[j]
    A[j]=m
    A[idx]=temp
print(A)






