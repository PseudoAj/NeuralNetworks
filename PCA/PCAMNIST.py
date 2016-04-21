__author__      = 	"Ajay Krishna Teja Kavuri"
__email__ 		= 	"ajkavuri@mix.wvu.edu"

import numpy as np 
import random
from mnist import MNIST
import matplotlib.pylab as plt

class PCAMNIST:
	

	#Initialization
	def __init__(self):
		#Load MNIST datset
		mnistData = MNIST('./mnistData')
		self.imgTrain,self.lblTrain=mnistData.load_training()
		self.imgTrainSmpl=self.imgTrain[:60000]
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

			#for img in self.imgTrainSmpl:
				#print img
		except:
			print Exception	
		

	#2. get the covaraince matrix for each digit
	def getCov(self):
		self.imgCov=[]
		dgtArr = np.asarray(self.imgTrainSmpl).T
		dgtCov = np.cov(dgtArr)
		self.imgCov.append(dgtCov)
		#for img in self.imgCov:
			#print img

	#3. get the eigen vectors from the covariance matrix
	def getEigen(self):
		self.eigVec=[]
		self.eigVal=[]
		dgtArr = np.asarray(self.imgCov)
		tmpEigVal,tmpEigVec=np.linalg.eig(dgtArr)
		self.eigVal.append(tmpEigVal.tolist())
		self.eigVec.append(tmpEigVec.tolist())

		#print "\nEigen values:\n"
		#for img in self.eigVal:
			#print img

		#print "\nEigen vectors:\n"
		#for img in self.eigVec:
			#print img
		
	#4. obtain the top most eigen vectors
	def sortEV(self):
		self.eigValArr = np.asarray(self.eigVal[0][0])
		self.eigVecArr = np.asarray(self.eigVec[0][0])
		self.srtdInd = np.argsort(self.eigValArr)[::-1]
		self.srtdEigValArr = self.eigValArr[self.srtdInd]
		self.srtdEigVecArr = self.eigVecArr[self.srtdInd]
		self.srtdEigVec = self.srtdEigVecArr.real.tolist()
		#print self.srtdEigValArr[0]
		#print np.asarray(self.eigVec).shape
		#print self.eigVec[self.srtdInd[0]]
		#print np.asarray(self.srtdEigVec).shape
		#for img in self.srtdEigVecArr:
			#print img
		#self.drawEig()

	#5. Plot the values
	def plotVal(self):
		plt.figure()
		plt.xlabel('Eigen count')
		plt.ylabel('Eigen value')
		plt.title('All Eigen values in descending order')
		x = np.arange(784)
		plt.plot(x,abs(self.srtdEigValArr[:784]),'--bo')
		plt.savefig("Plot"+str(random.randint(0,10000))+".png")
		plt.close()

	#6. Project a random image on to the eigen vectors
	def projectDigit(self,numFtrs):
		randIndx = random.randint(0,60000)
		self.drawChar(self.imgTrainSmpl[randIndx])
		self.randDgtArray = np.asarray(self.imgTrainSmpl[randIndx])
		self.projArr = self.srtdEigVecArr.T[:numFtrs]
		self.projFtrs = np.dot(self.randDgtArray,self.projArr.T)
		self.reconsDgt = np.dot(self.projFtrs,self.projArr)
		self.drawChar(self.reconsDgt)
		self.diffRecons = np.subtract(self.randDgtArray , self.reconsDgt)
		self.drawChar(self.diffRecons)
		print self.randDgtArray.shape
		print self.projArr.T.shape
		print self.projFtrs.shape
		print self.reconsDgt.shape
		print self.diffRecons.shape

	#Plot the feature values
	def plotFtrs(self):
		plt.figure()
		plt.xlabel('Feature Vector count')
		plt.ylabel('Feature Vector value')
		plt.title('Features Vector plot')
		#x = np.arange(784)
		plt.plot(self.projFtrs,'--bo')
		plt.savefig("Plot"+str(random.randint(0,10000))+".png")
		plt.close()
		

	#Function for plotting the eigen vectors
	def drawEig(self):
		for vec in self.srtdEigVecArr.T[:5]:
			self.drawEigV(vec)
		#for x in xrange(10):
			#self.drawEigV((self.srtdEigVecArr[:,x]).T)
		
	#Function for plotting specific vector
	def drawEigV(self,digit):
		plt.figure()
		fig=plt.imshow(np.asarray(digit).reshape(28,28),origin='upper')
		fig.set_cmap('gray_r')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.savefig("Eigen"+str(random.randint(0,10000))+".png")
		plt.close()

	#Draw a given character
	def drawChar(self,digit):
		plt.figure()
		fig=plt.imshow(np.asarray(digit).reshape(28,28),origin='upper')
		fig.set_cmap('gray_r')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.show()
		#plt.savefig("Digit"+str(random.randint(0,10000))+".png")
		plt.close()

	#Draw all images in sample
	def drawSmpl(self):
		for img in self.imgTrainSmpl:
			self.drawChar(img) 
	

asnmnt4=PCAMNIST()
asnmnt4.subMean()
asnmnt4.getCov()
asnmnt4.getEigen()
asnmnt4.sortEV()
asnmnt4.projectDigit(5)
asnmnt4.plotFtrs()
#asnmnt4.drawEig()
#asnmnt4.plotVal()
        