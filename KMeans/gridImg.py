#!/usr/bin/env python

"""
This code will make a grid of all the images
in the given folder.
"""

#Import the image package
from PIL import Image
from os import listdir
from os.path import isfile, join

class MakeGrid(object):
	#list all the files into list
	def __init__(self):
		self.folder= "/home/pseudoaj/GithubRepos/NeuralNetworks/KMeans/K80/"
		self.imgWidth=1600
		self.imgheight=2000
		self.files = [ f for f in listdir(self.folder) if isfile(join(self.folder, f)) ]
	
	#Function to show images
	def showImg(self):
		for img in self.files:
			thisImg = Image.open(self.folder+img)
			thisImg.show()

	def makeGrid(self):
		
		#Make a image to host all the images
		newImg = Image.new('RGBA', (self.imgWidth,self.imgheight))
		
		#Actuall grid making logic
		index = 0
		posX = 0
		posY = 0
		for i in xrange(10):
			for j in xrange(8):
				posX = j*200
				posY = i*200
				thisImg = Image.open(str(self.folder)+str(self.files[index]))
				thisImg.thumbnail((200,200))
				newImg.paste(thisImg,(posX,posY))
				print posX,posY
				index += 1 
		newImg.save("K80.png")


thisGrid=MakeGrid()
#thisGrid.showImg()
thisGrid.makeGrid()
