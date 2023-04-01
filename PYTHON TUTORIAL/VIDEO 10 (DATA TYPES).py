Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=2.5
type(num)
<class 'float'>
num=5
type(num)
<class 'int'>
num=6+9j
type(num)
<class 'complex'>
a=5.6
b=int(a)
b
5
c=float(num)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c=float(num)
TypeError: float() argument must be a string or a real number, not 'complex'
k=float(b)
k
5.0
k=6
c=complex(b,k)
c
(5+6j)
b<k
True
bool=b<k
bool
True
type(bool)
<class 'bool'>
f=k<b
f
False
type(f)
<class 'bool'>
int(True)
1
int(False)
0
int=[12,45,67,89]
type(int)
<class 'list'>
y={12,56,78,90,23}
type(y)
<class 'set'>
u=(12,45,76,89,09)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
u=(12,45,76,89,9,23,43)
type(u)
<class 'tuple'>
str='ebuka'
type(str)
<class 'str'>
range(10)
range(0, 10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(2,10,2))
[2, 4, 6, 8]
type(range(10))
<class 'range'>
r=[1:'Navin',2:'Hero',3:'Iphone',4:'Samsung']
SyntaxError: invalid syntax
r={1:'Navin',2:'Hero',3:'Iphone',4:'Samsung'}
type('r')
<class 'str'>
r
{1: 'Navin', 2: 'Hero', 3: 'Iphone', 4: 'Samsung'}
d.keys()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d.keys()
NameError: name 'd' is not defined. Did you mean: 'id'?
r.keys()
dict_keys([1, 2, 3, 4])
r.values()
dict_values(['Navin', 'Hero', 'Iphone', 'Samsung'])
r[1]
'Navin'
r.get(2)
'Hero'
