
#PANDAS
import pandas as pd
print(pd.__version__)
#Series Handle 1 dim array
data=pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
print(data.values)
print(type(data.values))
print(type(data))
data.index
print(data.index)
print(data['a'])
c=data['a':'c']
print(c)

#SERIES
gradedict={'A':4,'B':3.5,'C':3,'D':2.5}
grads=pd.Series(gradedict)
grads.values

marksdict={'A':85,'B':75,'C':65,'D':55}
marks=pd.Series(marksdict)
print(marks)
print(marks[0:2])


#DATA FRAME
D=pd.DataFrame({'Marks':marks,'Grades':grads})
D.T# To transpose
#print(D)
#D.values
#D.vlaues[2,0]
#D.colums
print(D)


#values
D['ScaledMarks']=100*(D['Marks']/90)
print(D)
del D['ScaledMarks']
print(D)
G=D[D['Marks']>70]
print(G)

#HANDLING MISSING DATA
R=pd.DataFrame([{'a':1,'b':2},{'b':3, 'c':4}])
print(R.T)
u=R.fillna(0)
print(u)

#INDEXING
# data[1] explicit referencing, use loc
# data[1:3] implicit referencing, use iloc
dt=pd.Series(['a','b','c'],index=[3,4,9])
print(dt[3])
print(dt[3:4])
p=dt.loc[3:4]
print(p)
o=dt.iloc[3:4]
print(o)

#PANDA CSV FILES



