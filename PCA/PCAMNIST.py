#!/usr/bin/env python

__author__      = 	"Ajay Krishna Teja Kavuri"
__email__ 		= 	"ajkavuri@mix.wvu.edu"

import numpy as np 
from mnist import MNIST
import matplotlib.pylab as plt
import random

class PCAMNIST:
	

	#Initialization
	def __init__(self):
		#Load MNIST datset
		mnistData = MNIST('./mnistData')
		self.imgTrain,self.lblTrain=mnistData.load_training()
		self.imgTrainSmpl=self.imgTrain[:50000]
		np.seterr(all='warn')


	#1. Subtract the mean because the PCA will work better
	def subMean(self):
		try:
			self.sumImg = np.empty([784,])
			#calculate the sum
			for img in self.imgTrainSmpl:
				imgArr = np.asarray(img)
				self.sumImg = np.add(imgArr,self.sumImg)
				
			#Calculate the mean array
			self.meanImg = self.sumImg/(len(self.imgTrainSmpl))
			self.meanImg = np.nan_to_num(self.meanImg)

			#subtract it out
			index=0
			for img in self.imgTrainSmpl:
				imgArr = np.asarray(img)
				self.imgTrainSmpl[index] = np.subtract(imgArr,self.meanImg).tolist()
				index += 1
		except:
			print Exception	
		

	#2. get the covaraince matrix for each digit
	def getCov(self):
		self.imgCov=[]
		dgtArr = np.asarray(self.imgTrainSmpl).T
		dgtCov = np.cov(dgtArr)
		print dgtCov.shape
		self.imgCov.append(dgtCov.tolist())
			
	
	def getEigen(self):
		self.eigVec=[]
		self.eigVal=[]
		dgtArr = np.asarray(self.imgCov)
		tmpEigVal,tmpEigVec=np.linalg.eig(dgtArr)
		self.eigVal.append(tmpEigVal.real.tolist())
		self.eigVec.append(tmpEigVec.real.tolist())
		print np.asarray(self.eigVec).shape
		print np.asarray(self.eigVal).shape
		for vec in self.eigVec.pop(0).pop(0):
			self.drawEigV(vec)


	def sortEV(self):
		self.srtdEigVec = np.asarray(self.eigVec).argsort().tolist()
		print np.asarray(self.srtdEigVec).shape
		#self.drawEigV(self.srtdEigVec[0][0][0])


	def plotVal(self):
		"""
		plt.figure()
		plt.scatter(np.asarray(self.eigVal).real)
		plt.show()
		"""

	def drawEig(self):
		self.srtdEigVec = self.srtdEigVec.pop(0).pop(0)
		for vec in self.srtdEigVec[:10]:
			print np.asarray(vec).shape
			self.drawEigV(vec)
		

	def drawEigV(self,digit):
		plt.figure()
		fig=plt.imshow(np.asarray(digit).T.reshape(28,28),origin='upper')
		fig.set_cmap('gray_r')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.savefig(str(random.randint(0,10000))+".png")
		#plt.show()
		plt.close()



	def drawChar(self,digit):
		plt.figure()
		fig=plt.imshow(np.asarray(digit).reshape(28,28),clim=(-1,1.0),origin='upper')
		fig.set_cmap('gray_r')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.show()
		plt.close()


	def drawSmpl(self):
		for img in self.imgTrainSmpl:
			self.drawChar(img) 

	def singleStep(self):
		self.val, self.vec = np.linalg.eig(np.cov(np.array(self.imgTrainSmpl).transpose()))
		self.srtd = np.argsort(self.val)[::-1]
		
		for vec in self.vec.real:
			self.drawEigV(vec.transpose())


asnmnt4=PCAMNIST()
asnmnt4.singleStep()
#asnmnt4.subMean()
#asnmnt4.getCov()
#asnmnt4.getEigen()
#asnmnt4.sortEV()
#asnmnt4.drawEig()
#asnmnt4.plotVal()
"""
asnmnt4.getSorted()
asnmnt4.printTopEigenVal()
"""
        