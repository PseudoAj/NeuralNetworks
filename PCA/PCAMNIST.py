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
		print np.asarray(self.eigVec).shape
		#print self.eigVec[self.srtdInd[0]]
		#print np.asarray(self.srtdEigVec).shape
		#for img in self.srtdEigVecArr:
			#print img
		#self.drawEig()

	#5. Plot the values
	def plotVal(self):
		plt.figure()
		x = np.arange(784)
		plt.plot(x,abs(self.srtdEigValArr[:784]))
		plt.savefig("Plot"+str(random.randint(0,10000))+".png")
		plt.close()

	def drawEig(self):
		for vec in self.srtdEigVecArr.T[:20]:
			self.drawEigV(vec)
		#for x in xrange(10):
			#self.drawEigV((self.srtdEigVecArr[:,x]).T)
		

	def drawEigV(self,digit):
		plt.figure()
		fig=plt.imshow(np.asarray(digit).reshape(28,28),origin='upper')
		fig.set_cmap('gray_r')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.savefig("Eigen"+str(random.randint(0,10000))+".png")
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
	

asnmnt4=PCAMNIST()
asnmnt4.subMean()
asnmnt4.getCov()
asnmnt4.getEigen()
asnmnt4.sortEV()
asnmnt4.drawEig()
#asnmnt4.plotVal()
        