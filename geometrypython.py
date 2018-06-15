import math
from turtle import *

##Law of Cosine
def mytriangle():

    firstside = int(input("please give me the first side length: "))
    secondside = int(input("please give me the second side length: "))
    firstangle = int(input("please give me the first angle: "))

    thirdside = (pow(firstside,2) + pow(secondside,2)) - ((2)*(firstside)*(secondside)*(math.cos(math.radians(firstangle))))
    thirdside1 = pow(thirdside,0.5)


    secondangle = math.acos((pow(secondside,2) - (pow(firstside,2)) - (pow(thirdside1,2)))/ ((-2)*(firstside)*(thirdside1)))
    secondangle1 = math.degrees(secondangle)


    thirdangle = - firstangle - secondangle1 + 180

    print (thirdangle)
    ##print(secondangle1)
    ##print(thirdside1)

    ## TURTLE DRAWING ##
    andres = Turtle()
    andres.goto(0,0)
    andres.down()
    andres.forward(firstside)
    andres.left(180 - secondangle1)
    andres.forward(thirdside1)
    andres.left(180 - firstangle)
    andres.forward(secondside)

if __name__=="__main__":
        mytriangle()
