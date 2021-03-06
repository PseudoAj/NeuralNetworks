__author__      = 	"Ajay Krishna Teja Kavuri"
__email__ 		= 	"ajkavuri@mix.wvu.edu"

import numpy as np 
from mnist import MNIST
import matplotlib.pylab as plt

class PCAMNIST:
	

	#Initialization
	def __init__(self):
		#Load MNIST datset
		mnistData = MNIST('./mnistData')
		self.imgTrain,self.lblTrain=mnistData.load_training()
		#self.imgTrainSmpl=self.imgTrain[:50000]
		self.imgTrainSmpl = [[2.5,2.4],[0.5,0.7],[2.2,2.9],[1.9,2.2],[3.1,3.0],[2.3,2.7],[2,1.6],[1,1.1],[1.5,1.6],[1.1,0.9]]
		np.seterr(all='warn')


	#1. Subtract the mean because the PCA will work better
	def subMean(self):
		try:
			self.sumImg = np.empty([2,])
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

		print "\nEigen values:\n"
		for img in self.eigVal:
			print img

		print "\nEigen vectors:\n"
		for img in self.eigVec:
			print img
		

	def sortEV(self):
		self.eigValArr = np.asarray(self.eigVal[0][0])
		self.eigVecArr = np.asarray(self.eigVec[0][0])
		self.srtdInd = np.argsort(self.eigValArr)[::-1]
		self.srtdEigVecArr = self.eigVecArr[self.srtdInd]
		self.srtdEigVal = self.srtdEigVecArr.real.tolist()
		for img in self.srtdEigVal:
			print img
		#self.drawEig()

	def plotVal(self):
		"""
		plt.figure()
		plt.scatter(np.asarray(self.eigVal).real)
		plt.show()
		"""

	def drawEig(self):
		for vec in self.srtdEigVec[:10]:
			self.drawEigV(vec)
		

	def drawEigV(self,digit):
		plt.figure()
		fig=plt.imshow(np.asarray(digit).reshape(28,28),origin='upper')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.show()
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
		print self.val


#asnmnt4=PCAMNIST()
#asnmnt4.singleStep()
asnmnt4=PCAMNIST()
#asnmnt4.subMean()
asnmnt4.getCov()
asnmnt4.getEigen()
asnmnt4.sortEV()
#asnmnt4.drawEig()
#asnmnt4.plotVal()
"""
asnmnt4.getSorted()
asnmnt4.printTopEigenVal()
"""
        