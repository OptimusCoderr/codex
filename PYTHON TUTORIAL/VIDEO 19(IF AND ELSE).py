x=8
r=x%2
if r==0:
    print('it is even')
else:
    print('odd')

# if and nested if
a=int(input("enter a number"))
c=a%2
if c==0:
    print("even")
    if a>5:
        print('no geater than 5')
    else:
        print('not greater than 5')
else:
    print('odd')


# Other ways to use the if statement
#elif means else if
o=int(input('input an integer'))

if(o==1):
    print('Nom is 1')
elif(o==2):
    print('Nom is 2')
elif(o==3):
    print('Nom is 3')
elif(o==4):
    print('Nom is 4')
if(o==5):
    print('Nom is 5')
else:
    print('invalid input')


