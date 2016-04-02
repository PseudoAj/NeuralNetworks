
# coding: utf-8

# # K Means over MNIST writted by 
# ## Ajay Krishna Teja Kavuri (@pseudoaj)

# First, we have to load the mnist dataset, for which I am using a python-mnist project(https://github.com/sorki/python-mnist)

# In[1]:

from mnist import MNIST
import matplotlib.pylab as plt
import numpy as np
import random
import collections


# Now we will write our class for the processing and initialise with training, testing and K array values data

# In[2]:

class KMeansMNIST:
    
    def __init__(self,k):
        #Define k value
        self.k=k
        #Load MNIST datset
        mnistData=MNIST('./mnistData')
        self.imgTrain,self.lblTrain=mnistData.load_training()
        self.imgTest,self.lblTest=mnistData.load_testing()
        #Initialize the random centroids
        self.imgCen=[]
        for c in xrange(self.k):
            self.imgCen.append([random.randint(0,255) for d in xrange(784)])
        
        


# Optional, just a random function for confirmation

# In[3]:

def verifyLength(self):
    print str(len(self.imgTrain))+"\t"+str(len(self.imgTest))


# Draw the character when passed an array of digits

# In[4]:

def drawChar(self,digit):
    plt.figure()
    fig = plt.imshow(np.asarray(digit).reshape(28,28))
    fig.set_cmap('gray_r')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()
    plt.close()


# Draw the centroids that are randomly initialized

# In[5]:

def drawCentroids(self):
    for i in xrange(self.k):
        drawChar(self,self.imgCen[i])


# Cluster the data for each data point

# In[6]:

def clusterData(self):
    self.map=collections.defaultdict(list)
    for digit in self.imgTrain:
        clstr=findCluster(self,digit)
        clstrIndex=self.imgCen.index(clstr)
        digitIndex=self.imgTrain.index(digit)
        mapDigits(self,clstrIndex,digitIndex)
    print len(self.map)


# In[7]:

def mapDigits(self,clstrIndex,digitIndex):
    self.map[clstrIndex].append(digitIndex)


# Pass each point to the function and calculate the mean 

# In[8]:

def findCluster(self,digit):
    minDist=float("inf")
    minClstr=[]
    for clstr in self.imgCen:
        tmpDist=getEcldnDist(self,digit,clstr)
        if tmpDist<=minDist:
            minDist=tmpDist
            minClstr=clstr
    return minClstr
        


# In[9]:

def getEcldnDist(self,digit,clstr):
    dist = np.linalg.norm(np.asarray(digit)-np.asarray(clstr))
    return dist
        
             


# Initialize the class and run the logic, basic logic of the K means involes:
# 1. Choose N input points
# 2. Choose K random centroids
# 3. Repeat until converges: 
#  * For each point:
#    1. Assign to the closest project(mean squared distance)
#  * For each centroid:
#    1. Update the centroid by calculating the mean
# 4. Stop
# 

# In[10]:

myKmeans=KMeansMNIST(10)
clusterData(myKmeans)


# In[ ]:



