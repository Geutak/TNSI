from turtle import *
def koch(l,n):
    
    if n<=0:
        forward(l)
    else:
        koch(l/3,n-1)
        right(300)
        koch(l/3,n-1)
        right(120)
        koch(l/3,n-1)
        right(300)
        koch(l/3,n-1)

def etoile_koch(l,n):
    speed(0)
    up()
    setpos((-350,150))
    down()
    koch(l,n)
    right(120)
    koch(l,n)
    right(120)
    koch(l,n)
    done()


print(etoile_koch(100,2))