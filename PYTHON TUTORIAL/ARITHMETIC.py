#PYTHON TUTORIALS FOR DATA SCIENCE
a=True
b=True
c= False

print(a and b)
print (a and c)
print(a or b)
print(a or c)
print(type(a))

print(not((a and b) or (c or b)))

# Comparisons
print(2<3)
print(((not(2!=3)and True)) or (False and True))

#SOME USEFUL FUNCTIONS
# rounds up a number
print(round(5.678923))
print(round(3.84499384,3))

#does a division and returns the quotient and remainder/mod in tuple form
print(divmod(27,5))
a=divmod(34,9)
print(a)
print(type(a))

#isinstance() returns True, if the first argument is an instance of that class
print(isinstance(1,int))
print(isinstance(1.0,(int,float)))
print(isinstance(1.0,int))

# pow(x,y,z) x raised to the power y and remainder by z
print(pow(2,4))
print(pow(2,4,7))

# input function
x= input("Enter a number :")
print(type(x))
x=int(x) #to change a data type
print(type(x))
a= float(input("Enter  any number: "))
help(pow)# to help on how to use a function



