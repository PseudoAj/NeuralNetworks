#!/usr/bin/env python

"""
This code will make a grid of all the images
in the given folder.
"""

__author__ = "Ajay Krishna Teja Kavuri"
__copyright__ = "copyright 2016"
__email__ = "ajaykrishnateja@gmail.com"


#Import the image package
from PIL import Image
from os import listdir
from os.path import isfile, join

class MakeGrid(object):
	#list all the files into list
	def __init__(self):
		print("-------------------------------------------------------")
		print("-------------------------------------------------------")
		print("Welcome to Grid Image\n")
		print("-------------------------------------------------------")
		print("-------------------------------------------------------")
		self.folder = raw_input("Please input the folder with images\nexample: /home/pseudoaj/GithubRepos/NeuralNetworks/KMeans/K80/ \n")
		self.folder = str(self.folder)
		#self.folder = "/home/pseudoaj/GithubRepos/NeuralNetworks/KMeans/K80/"
		self.files = [ f for f in listdir(self.folder) if isfile(join(self.folder, f)) ]
		self.fCount=len(self.files)
		print("-------------------------------------------------------")
		print("-------------------------------------------------------")
		print("There are "+str(self.fCount)+" images in directory\n")
		print("-------------------------------------------------------")
		print("-------------------------------------------------------")
		self.grdW = raw_input("Please input grid Width: ")
		self.grdH = raw_input("Please input grid height: ")
		self.imgWidth=200*int(self.grdW)
		self.imgheight=200*int(self.grdH)
		

	
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
		for j in xrange(int(self.grdH)):
			for i in xrange(int(self.grdW)):
				posX = i*200
				posY = j*200
				thisImg = Image.open(str(self.folder)+str(self.files[index]))
				thisImg.thumbnail((200,200))
				newImg.paste(thisImg,(posX,posY))
				print posX,posY
				index += 1 
		newImg.save("K80.png")


thisGrid=MakeGrid()
#thisGrid.showImg()
thisGrid.makeGrid()
