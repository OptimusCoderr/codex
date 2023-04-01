"""""
Given a list of number i.e [1,2,3,4,-5,7,9,3,2] make another list that contains all the items in sorted order from min to max
i.e your result will be another list like [-5,1,2,2,3,7,9]
"""""
def findmin(L,sidx):
    m=L[sidx]
    idx=sidx
    i=0
    for i in range(sidx,len(L)):
        x=L[i]
        if x<m:
             m=x
             idx=i
        else:
            pass
        i+=1

    return m,idx



def swapvals(L,idx1,idx2):
    tmp=L[idx1]
    L[idx1]=L[idx2]
    L[idx2]=tmp
    return L




def sort(L):
    if not(checkifnotnumeric2(L)):
        print ("List doesn not contain numeric values")
        return
    else:
        c=0
        for x in L:
            m,idx=findmin(L,c)
            L=swapvals(L,c,idx)
            c+=1
    return L

def checkifnotnumeric2(L):
    retvalue=True
    for x in L:
        if not(isinstance(x,(int,float))):
            return False
        return True

L=[2,3,4,5,7]
a=sort(L)

L2= sort(L)
print(L)


A=[1,23,4,6,7,-8,-99]
A.sort()
print(A)
