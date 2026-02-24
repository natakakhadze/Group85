import math
from turtle import *

def hearta(k):
    return 15math.sin(k)*5
def heartb(k):
    return 12math.cos(k)-5math.cos(2k)-2math.cos(3k)-math.cos(4k)
speed(300)
bgcolor('black')
for i in range(360):
    goto(hearta(i)20, heartb(i)20)
    for j in range(5):
        color('red')
    goto(0,0)
done()
