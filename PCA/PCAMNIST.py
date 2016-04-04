__author__      = 	"Ajay Krishna Teja Kavuri"
__email__ 		= 	"ajkavuri@mix.wvu.edu"

import numpy as np 
from mnist import MNIST
import matplotlib.pylab as plt

class PCAMNIST:
	
	def __init__(self):
		#Load MNIST datset
		mnistData = MNIST('./mnistData')
		self.imgTrain,self.lblTrain=mnistData.load_training()
		self.imgTrainSmpl=self.imgTrain[:100]

	def getCov(self):
		self.imgTrainCov=[]
		for digit in self.imgTrain:
			self.imgTrainCov.append(np.cov(np.asarray(digit)).tolist()) 
		
	def drawChar(self,digit):
		plt.figure()
		fig=plt.imshow(np.asarray(digit).reshape(28,28),clim=(-1,1.0),origin='upper')
		fig.set_cmap('gray_r')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.show()
		plt.close()

	def getEigen(self):
		self.eigVec=[]
		self.eigVal=[]
		for digit in self.imgTrain:
			tmpEigVal,tmpEigVec=np.linalg.eig(np.asarray(digit).reshape((28,28)))
			self.eigVal.append(tmpEigVal.tolist())
			self.eigVec.append(tmpEigVec.tolist())
	def getSorted(self):
		self.sortEigVal=np.sort(self.eigVal)

	def printTopEigenVal(self):
		for val in self.sortEigVal[59980:60000]:
			print val

asnmnt4=PCAMNIST()
asnmnt4.getCov()
asnmnt4.getEigen()
asnmnt4.getSorted()
asnmnt4.printTopEigenVal()

        