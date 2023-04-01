def checkifnotnumeric(*args):
    retvalue=True
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
        return True


def addallvals(*args):
    s=0
    for x in args:
        s+=x
    return s

myname="python course"