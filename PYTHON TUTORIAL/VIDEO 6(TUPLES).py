Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tup = (23,45,97,61)
tup
(23, 45, 97, 61)
tup[0]
23
tup.count()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup.count()
TypeError: tuple.count() takes exactly one argument (0 given)
tup.index(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup.index(1)
ValueError: tuple.index(x): x not in tuple
s={13,57,90,96,42}
s
{96, 90, 57, 42, 13}
s.add(22)
s
{96, 90, 22, 57, 42, 13}
data={1:'Navin',2:'Ebuka',3:'Gppgle',4:'144566'}
data[2]
'Ebuka'
data[3]
'Gppgle'
data[5]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data[5]
KeyError: 5
data.get(1)
'Navin'
data.get(5)
print(data.get(5))
None
data.get(6,'Notfound')
'Notfound'
data.get(1,'Not available')
'Navin'
keys=['Navin','Kira','Ebuka']
values=['python','C++','Js']
data=dict(zip(keys,values))
print(data)
{'Navin': 'python', 'Kira': 'C++', 'Ebuka': 'Js'}
data['Ebuka']
'Js'
data['Praise']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    data['Praise']
KeyError: 'Praise'
data['Kene']= 'React'
print(data)
{'Navin': 'python', 'Kira': 'C++', 'Ebuka': 'Js', 'Kene': 'React'}
del data('Navin')
SyntaxError: cannot delete function call
del data['Navin']
print(data)
{'Kira': 'C++', 'Ebuka': 'Js', 'Kene': 'React'}
prog= {'Js':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse']
       
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
prog= {'Js':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
       
prog['Js']
       
'Atom'
prog['Java']
       
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
prog['Java']['JEE']
       
'Eclipse'
prog['Python'][0]
       
'Pycharm'
