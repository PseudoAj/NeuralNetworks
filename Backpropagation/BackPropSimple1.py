__author__ = 'Ajay Krishna Teja K'

import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

class NNetwork:


    #Initialize the neural network
    def init(self):

        #Define the network topology
        self.nInput=3
        self.nHidden=3
        self.nOutput=1
        self.lRate=0.5

        #Initial weights and bias
        self.w14=2
        self.w15=4
        self.w16=2.2
        self.w24=1.8
        self.w25=0.7
        self.w26=1.3
        self.w34=2.6
        self.w35=0.35
        self.w36=1.9
        self.w47=0.9
        self.w57=2.3
        self.w67=1.1
        self.b4=1.4
        self.b5=1.7
        self.b6=0.6
        self.b7=2.4
        """
        self.w14=2.8484343063
        self.w15=4.07720156962
        self.w16=2.71418184289
        self.w24=2.96215464829
        self.w25=1.95885995334
        self.w26=2.30127383154
        self.w34=3.24850646456
        self.w35=1.73624227555
        self.w36=2.54943375241
        self.w47=0.8756557109
        self.w57=2.29183053186
        self.w67=1.08496956975
        self.b4=5.70280867487
        self.b5=6.91034185324
        self.b6=6.04883924918
        self.b7=-5.2968584407
        """
    def defIO(self,x1,x2,x3,out):
        self.x1=x1
        self.x2=x2
        self.x3=x3
        self.out=out



    def feedForward(self):
        #Output calcuation at the hidden layer
        self.o4=self.sigmod(float(self.w14*self.x1+self.w24*self.x2+self.w34*self.x3+self.b4))
        self.o5=self.sigmod(float(self.w15*self.x1+self.w25*self.x2+self.w35*self.x3+self.b5))
        self.o6=self.sigmod(float(self.w16*self.x1+self.w26*self.x2+self.w36*self.x3+self.b6))

        #Output calculation at the outut layer
        self.o7=self.sigmod(float(self.w47*self.o4+self.w57*self.o5+self.w67*self.o6+self.b7))
        #print "Feed forward results:\n"+str(self.o4)+"\n"+str(self.o5)+"\n"+str(self.o6)+"\n"+str(self.o7)


    def backProp(self):

        #Estimate the error at the output
        self.ErrAtOut=float(self.o7*(1-self.o7)*(self.out-self.o7))
        self.meanErrSqOut=float(math.pow((self.out-self.o7),2)/2)

        #Estimate error at hidden layer
        self.ErrAtH4=float(self.o4*(1-self.o4)*(self.o7*self.w47))
        self.ErrAtH5=float(self.o5*(1-self.o5)*(self.o7*self.w57))
        self.ErrAtH6=float(self.o6*(1-self.o6)*(self.o7*self.w67))
        #print "Back propogation Error:\n"+str(self.ErrAtOut)+"\n"+str(self.ErrAtH4)+"\n"+str(self.ErrAtH5)+"\n"+str(self.ErrAtH6)



        #Back propagate the weights and bias
        self.w14=self.w14+float(self.lRate*self.ErrAtH4*self.x1)
        self.w15=self.w15+float(self.lRate*self.ErrAtH5*self.x1)
        self.w16=self.w16+float(self.lRate*self.ErrAtH6*self.x1)
        self.w24=self.w24+float(self.lRate*self.ErrAtH4*self.x2)
        self.w25=self.w25+float(self.lRate*self.ErrAtH5*self.x2)
        self.w26=self.w26+float(self.lRate*self.ErrAtH6*self.x2)
        self.w34=self.w34+float(self.lRate*self.ErrAtH4*self.x3)
        self.w35=self.w35+float(self.lRate*self.ErrAtH5*self.x3)
        self.w36=self.w36+float(self.lRate*self.ErrAtH6*self.x3)
        self.w47=self.w47+float(self.lRate*self.ErrAtOut*self.ErrAtH4)
        self.w57=self.w57+float(self.lRate*self.ErrAtOut*self.ErrAtH5)
        self.w67=self.w67+float(self.lRate*self.ErrAtOut*self.ErrAtH6)
        self.b4=self.b4+float(self.lRate*self.ErrAtH4)
        self.b5=self.b5+float(self.lRate*self.ErrAtH5)
        self.b6=self.b6+float(self.lRate*self.ErrAtH6)
        self.b7=self.b7+float(self.lRate*self.ErrAtOut)

        return self.meanErrSqOut
        #return self.ErrAtOut

    def printOut(self):
        print float(self.o7)

    def printNetworkParam(self):
        print "Network Configuration:\n"+str(self.w14)+"\t"+str(self.w15)+"\t"+str(self.w16)+"\n"+str(self.w24)+"\t"+str(self.w25)+"\t"+str(self.w26)+"\n"+str(self.w34)+"\t"+str(self.w35)+"\t"+str(self.w36)+"\n"+str(self.w47)+"\t"+str(self.w57)+"\t"+str(self.w67)+"\n"+str(self.b4)+"\t"+str(self.b5)+"\t"+str(self.b6)+"\t"+str(self.b7)

    def getError(self):
        return self.meanErrSqOut

    def getOutW(self):
        return self.w47,self.w57,self.w67

    def sigmod(self,netValue):
        return round(float(1.0/float(1+math.exp(-netValue))),4)

myNN=NNetwork()
myNN.init()
"""
myNN.init()
myNN.defIO(0,0,0,0)
myNN.feedForward()
myNN.printOut()
myNN.defIO(0,0,1,1)
myNN.feedForward()
myNN.printOut()
myNN.defIO(0,1,0,1)
myNN.feedForward()
myNN.printOut()
myNN.defIO(0,1,1,0)
myNN.feedForward()
myNN.printOut()
myNN.defIO(1,0,0,1)
myNN.feedForward()
myNN.printOut()
myNN.defIO(1,0,1,0)
myNN.feedForward()
myNN.printOut()
myNN.defIO(1,1,0,0)
myNN.feedForward()
myNN.printOut()
myNN.defIO(1,1,1,1)
myNN.feedForward()
myNN.printOut()

"""
iterationArr=[]
error=[]
oW1=[]
oW2=[]
oW3=[]

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
    w1,w2,w3=myNN.getOutW()
    oW1.append(w1)
    oW2.append(w2)
    oW3.append(w3)


myNN.printNetworkParam()
plt.plot(iterationArr,error,'-o')
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(oW1,oW2, oW3, s=20,c='b', depthshade=True)
ax.set_xlabel('Weight between 4 and 7')
ax.set_ylabel('Weight between 5 and 7')
ax.set_zlabel('Weight between 6 and 7')
plt.show()