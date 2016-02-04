__author__ = 'Ajay Krishna Teja K'
#
# This program is to detect the XOR problem associate with the neral network, here are the attributes:
#1. Inputs: x1 and x2
#2. Each layer has a function of it's own and declare the inputs likewise, in this program we have one perceptron(p1) and two inputs with a bias

def hiddenLayer1(x1,x2):
    p1=x1+x2-0.5
    return hardBound(p1)

def hiddenLayer2(x1,x2):
    p1=x1+x2-1.5
    return hardBound(p1)

#3. Output layer equations can be added, in this case it is connected to input so we take input from lower layer
def outPutLayer(h1,h2):
    out=h1-h2-0.5
    return hardBound(out)

#4. stepFinction definition, any other equation can be defined here
def hardBound(x):
    if x > 0:
        return 1
    else:
        return 0

#5. Getting together the stack to solve the problem
def nNStack(x1,x2):
    h1=hiddenLayer1(x1,x2)
    h2=hiddenLayer2(x1,x2)
    #print str(h1)+"\n"
    out=outPutLayer(h1,h2)
    #print str(out)+"\n"
    return out

def checkXOR(c1,c2,c3,c4):
    if c1==0 & c1==1 & c1==1 & c1==0:
        return True
    else:
        return False

def hw1problem2a():
    #6. Check for the XOR truth table that returns 0 1 1 0 for the inputs 0 0, 0 1, 1 0, 1 1
    #Calling my program
    #Case 1
    c1= nNStack(0,0)
    #Case 2
    c2= nNStack(0,1)
    #Case 3
    c3= nNStack(1,0)
    #Case 4
    c4= nNStack(1,1)
    #Check the XOR
    xor=checkXOR(c1,c2,c3,c4)
    #Print Cases
    print str(xor)

#Execute the problem
hw1problem2a()