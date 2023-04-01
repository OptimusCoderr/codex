Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2+3
5
9-8
1
4*6
24
8/4
2.0
5/2
2.5
5//2
2
10%3
1
2^3
1
2**3
8
(2)^6
4
'navin'
'navin'
print('ebuak
      
SyntaxError: unterminated string literal (detected at line 1)
print('Ebuka')
      
Ebuka
print("Navin's laptop")
      
Navin's laptop
print('ebuka"laptop" yep')
      
ebuka"laptop" yep
print('navin\'s "laptop" ')
      
navin's "laptop" 
print(r'c:\docs\navin')
      
c:\docs\navin
e=2
      
print(e)
      
2
x=12+e
      
x
      
14
_+5
      
19
name= 'youtube'
      
name
      
'youtube'
name[1]
      
'o'
name[0]
      
'y'
name[0:3]
      
'you'
name[-1]
      
'e'
'my'+ name[3:]
      
'mytube'
myname='anulunko'
      
len(myname)
      
8
nums=[1 2 3 4 5 6]
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
nums=[1,2,3,4,5,6]
      
nums[0]
      
1
names= ['mum','dad','after']
      
names[0]
      
'mum'
values=[9.5,'name',9]
      
mil=[nums,names]
      
mil
      
[[1, 2, 3, 4, 5, 6], ['mum', 'dad', 'after']]
nums.append(45)
      
nums
      
[1, 2, 3, 4, 5, 6, 45]
nums.clear
      
<built-in method clear of list object at 0x0000019211E35340>
nums
      
[1, 2, 3, 4, 5, 6, 45]
nums.clear(2)
      
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    nums.clear(2)
TypeError: list.clear() takes no arguments (1 given)
nums.insert(22,9)
      
nums
      
[1, 2, 3, 4, 5, 6, 45, 9]
nums.clear(2,2)
      
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    nums.clear(2,2)
TypeError: list.clear() takes no arguments (2 given)
nums.clear()
      
nums
      
[]
nam=[1,2,3,4,5,6,7,89]
      
nam.pop(1)
      
2
num
      
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    num
NameError: name 'num' is not defined. Did you mean: 'nums'?
nam
      
[1, 3, 4, 5, 6, 7, 89]
nam.pop()
      
89
del nam
      
nam
      
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    nam
NameError: name 'nam' is not defined. Did you mean: 'name'?
jan= [1,2,3,4,5,6,7,88,9,5]
      
min(jan)
      
1
max(jan)
      
88
mean(jan)
      
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    mean(jan)
NameError: name 'mean' is not defined
sum(jan)
      
130
nums.sort()
      
nums
      
[]
jan.sort()
      
jan
      
[1, 2, 3, 4, 5, 5, 6, 7, 9, 88]
