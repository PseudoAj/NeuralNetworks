__author__ = 'Ajay Krishna Teja K'

import math
import numpy
import matplotlib.pyplot as plt

class NNetwork:
    #Initialize the neural network
    def init(self):

        #Define the network topology
        self.nInput=7
        self.nOutput=1
        self.lRate=0.5

        #Initial weights and bias
        self.w18=2
        self.w28=1.7
        self.w38=3.6
        self.w48=0.5
        self.w58=4
        self.w68=1.35
        self.w78=0.9
        self.b8=2.9

    def defIO(self,x1,x2,x3,out):
        self.x1=x1
        self.x2=x2
        self.x3=x3
        self.x4=numpy.dot(x1,x2)
        self.x5=numpy.dot(x1,x3)
        self.x6=numpy.dot(x2,x2)
        self.x7=x1*x2*x3
        self.out=out

    def feedForward(self):
        #Output calculation at the outut layer
        self.o1=self.sigmod(float(self.w18*self.x1+self.w28*self.x2+self.w38*self.x3+self.w48*self.x4+self.w58*self.x5+self.w68*self.x6+self.w78*self.x7+self.b8))
        #print "Feed forward results:\n"+str(self.o4)+"\n"+str(self.o5)+"\n"+str(self.o6)+"\n"+str(self.o7)

    def getError(self):
        return self.meanErrSqOut

    def backProp(self):

        #Estimate the error at the output
        self.ErrAtOut=float(self.o1*(1-self.o1)*(self.out-self.o1))
        self.meanErrSqOut=float(math.pow((self.out-self.o1),2)/2)

        #Back propagate the weights and bias
        self.w18=self.w18+float(self.lRate*self.ErrAtOut*self.x1)
        self.w28=self.w28+float(self.lRate*self.ErrAtOut*self.x2)
        self.w38=self.w38+float(self.lRate*self.ErrAtOut*self.x3)
        self.w48=self.w48+float(self.lRate*self.ErrAtOut*self.x4)
        self.w58=self.w58+float(self.lRate*self.ErrAtOut*self.x5)
        self.w68=self.w68+float(self.lRate*self.ErrAtOut*self.x6)
        self.w78=self.w78+float(self.lRate*self.ErrAtOut*self.x7)
        self.b8=self.b8+float(self.lRate*self.ErrAtOut)

        return self.meanErrSqOut

    def printNetworkParam(self):
        print "Network Configuration:\n"+str(self.w18)+"\t"+str(self.w28)+"\t"+str(self.w38)+"\n"+str(self.w48)+"\t"+str(self.w58)+"\t"+str(self.w68)+"\n"+str(self.w78)+"\t"+str(self.b8)

    def sigmod(self,netValue):
        return round(float(1.0/float(1+math.exp(-netValue))),4)

myNN=NNetwork()
myNN.init()
iterationArr=[]
error=[]
itr=10
for x in xrange(100):

    for y in xrange(itr):
        myNN.defIO(1,1,1,1)
        myNN.feedForward()
        myNN.backProp()


    for y in xrange(itr):
        myNN.defIO(0,1,0,1)
        myNN.feedForward()
        myNN.backProp()

    for y in xrange(itr):
        myNN.defIO(0,0,1,1)
        myNN.feedForward()
        myNN.backProp()

    for y in xrange(itr):
        myNN.defIO(1,0,0,1)
        myNN.feedForward()
        myNN.backProp()

    for y in xrange(itr):
        myNN.defIO(1,1,0,0)
        myNN.feedForward()
        myNN.backProp()

    for y in xrange(itr):
        myNN.defIO(1,0,1,0)
        myNN.feedForward()
        myNN.backProp()

    for y in xrange(itr):
        myNN.defIO(0,1,1,0)
        myNN.feedForward()
        myNN.backProp()

    for y in xrange(itr):
        myNN.defIO(0,0,0,0)
        myNN.feedForward()
        myNN.backProp()


    error.append(myNN.getError())
    iterationArr.append(x)
myNN.printNetworkParam()
plt.plot(iterationArr,error,'-o')
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()

"""
ecount=0
epochs=100
meanEr1=0
meanEr2=0
meanEr3=0
meanEr4=0
meanEr5=0
meanEr6=0
meanEr7=0
meanEr8=0
meanErr=1000
iterationArr=[]
error=[]
while ecount<epochs:
    iteration=10
    icount=0
    if meanErr<0.0005:
        break
    while icount<iteration:
        myNN.defIO(0,0,0,0)
        myNN.feedForward()
        meanEr1=myNN.backProp()
        #print meanErr
        icount=icount+1

    while icount<iteration:
        myNN.defIO(0,0,1,1)
        myNN.feedForward()
        meanEr2=myNN.backProp()
        #print meanErr
        icount=icount+1

    while icount<iteration:
        myNN.defIO(0,1,0,1)
        myNN.feedForward()
        meanEr3=myNN.backProp()
        #print meanErr
        icount=icount+1

    while icount<iteration:
        myNN.defIO(0,1,1,0)
        myNN.feedForward()
        meanEr4=myNN.backProp()
        #print meanErr
        icount=icount+1

    while icount<iteration:
        myNN.defIO(1,0,0,1)
        myNN.feedForward()
        meanEr5=myNN.backProp()
        #print meanErr
        icount=icount+1

    while icount<iteration:
        myNN.defIO(1,0,1,0)
        myNN.feedForward()
        meanEr6=myNN.backProp()
        #print meanErr
        icount=icount+1

    while icount<iteration:
        myNN.defIO(1,1,0,0)
        myNN.feedForward()
        meanEr7=myNN.backProp()
        #print meanErr
        icount=icount+1

    while icount<iteration:
        myNN.defIO(1,1,1,1)
        myNN.feedForward()
        meanEr8=myNN.backProp()
        #print meanErr
        icount=icount+1

    meanErr=float(meanEr1+meanEr2+meanEr3+meanEr4+meanEr5+meanEr6+meanEr7+meanEr8)/8
    ecount=ecount+1
    iterationArr.append(ecount)
    error.append(meanErr)

plt.plot(iterationArr,error,'-o')
plt.show()
"""